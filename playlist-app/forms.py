"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name", validators=[
        InputRequired(message="Playlist Name cannot be blank")])
    description = StringField("Description")


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Song Title", validators=[
        InputRequired(message="Song Title cannot be blank")])
    artist = StringField("Song Artist", validators=[
        InputRequired(message="Song Artist cannot be blank")])


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
