import pandas as pd
from config import db

from . import TrackModel

class TrackController:
    def __init__(self) -> None:
        self.__track = TrackModel()
        pass

    def insert_data(self, df: pd.DataFrame):
        try:
            df.to_sql(name=self.__track.__tablename__, con=db.engine, if_exists="replace", index=False)
        except:
            print("Something went wrong!!")
    
    def retrieve_data(self):
        try:
            tracks = self.__track.query.all()
            return tracks
        except:
            print("Something went wrong to retrieve data")