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
