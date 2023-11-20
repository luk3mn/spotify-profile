from ..ext.database import db

class TrackModel(db.Model):
    __tablename__ = "tb_track"

    song_id = db.Column(db.String(200), primary_key=True)
    song = db.Column(db.String(200))
    artist = db.Column(db.String(200))
    album = db.Column(db.String(200))
    release = db.Column(db.String(200))
    popularity = db.Column(db.String(200))
    # popularity = db.Column(db.Integer)
    preview_url = db.Column(db.String(200))
    images_url = db.Column(db.String(200))
    spotify_song = db.Column(db.String(200))
    spotify_artist = db.Column(db.String(200))
    spotify_album = db.Column(db.String(200))

    def __repr__(self):
        return 'Id <%r>' % self.song_id
        # return f'{self.song_id}, {self.song}'

class ProfileModel(db.Model):
    __tablename__ = "tb_profile"

    spotify_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))
    profile = db.Column(db.String(200))
    spotify_profile = db.Column(db.String(200))

    def __repr__(self) -> str:
        return 'Id <%r>' % self.spotify_id

class FollowedArtistsModel(db.Model):
    __tablename__ = "tb_followed_artists"

    id = db.Column(db.String(100), primary_key=True)
    artist = db.Column(db.String(50))
    genres = db.Column(db.String(200))
    popularity = db.Column(db.Integer)
    image_artist = db.Column(db.String(200))
    spotify_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Id <%r>" % self.id
