from sqlalchemy import text
import pandas as pd
from ..ext.database import db

# from . import ProfileModel, FollowedArtistsModel

class ApplicationController:
    def __init__(self, model: db.Model) -> None:
        self.__model = model

    def insert_data(self, df: pd.DataFrame):
        try:
            df.to_sql(name=self.__model.__tablename__, con=db.engine, if_exists="replace", index=False)
        except Exception:
            return "Something went wrong!!"

    def retrieve_data(self):
        try:
            data = self.__model.query.all()
            return data
        except Exception:
            return "Something went wrong to retrieve data"

    def group_by_track(self) -> object:
        query = db.session.execute(text("""
            SELECT  name,
                    artist,
                    album,
                    popularity,
                    spotify_url,
                    preview_url,
                    album_url
                    release,
                    image,
                    count(track_id) as "played"
            from tb_recently_played
            GROUP BY name, album, artist, release, image, popularity, spotify_url, preview_url, album_url
            ORDER BY played DESC
        """)).all()

        return query

    def most_played_track(self) -> object:
        query = db.session.execute(text("""
            SELECT * FROM (
                SELECT  name, 
                        image, 
                        artist, 
                        album, 
                        release, 
                        popularity, 
                        spotify_url,
                        count(track_id) as "played"
                FROM tb_recently_played
                GROUP BY name, image, track_id, artist, album, release, popularity, spotify_url
                ORDER BY played DESC
            ) AS "most_played"
            WHERE played = (
                SELECT max(played) FROM (
                    SELECT count(track_id) as "played"
                    FROM tb_recently_played
                    GROUP BY track_id
                ) AS "max_played"
            )
        """)).all()

        return query

    def latest_played_track(self) -> object:
        query = db.session.execute(text("""
            SELECT * FROM tb_recently_played
            WHERE played_at = (
                SELECT max(played_at)
                FROM tb_recently_played
            )
        """)).all()

        return query
