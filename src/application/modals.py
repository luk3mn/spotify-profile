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

class ProfileModel(db.Model):
    __tablename__ = "tb_profile"

    spotify_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))
    profile = db.Column(db.String(200))
    spotify_profile = db.Column(db.String(200))

    def __repr__(self) -> str:
        return 'Id <%r>' % self.spotify_id

class ArtistModel(db.Model):
    __tablename__ = "tb_artist"

    id = db.Column(db.String(100), primary_key=True)
    artist = db.Column(db.String(50))
    genres = db.Column(db.String(200))
    popularity = db.Column(db.Integer)
    image_artist = db.Column(db.String(200))
    spotify_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Id <%r>" % self.id

class PlaylistModel(db.Model):
    __tablename__ = "tb_playlist"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    owner = db.Column(db.String(50))
    total = db.Column(db.Integer)
    spotify_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Name <%r>" % self.name

class RecentlyPlayedModel(db.Model):
    __tablename__ = "tb_recently_played"

    played_at = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    track_id = db.Column(db.String(100))
    artist = db.Column(db.String(50))
    album = db.Column(db.String(50))
    release = db.Column(db.String(20))
    popularity = db.Column(db.Integer)
    preview_url = db.Column(db.String(200))
    spotify_url = db.Column(db.String(200))
    album_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Name <%r>" % self.name

class RecommendationModel(db.Model):
    __tablename__ = "tb_recommendation"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    total = db.Column(db.Integer)
    owner = db.Column(db.String(40))
    spotify_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Name <%r>" % self.name

class DiscoverWeeklyModel(db.Model):
    __tablename__ = "tb_discover_weekly"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(200))
    total = db.Column(db.Integer)
    owner = db.Column(db.String(40))
    spotify_url = db.Column(db.String(200))

    def __repr__(self) -> str:
        return "Name <%r>" % self.name
