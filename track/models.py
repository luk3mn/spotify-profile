from config import db

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