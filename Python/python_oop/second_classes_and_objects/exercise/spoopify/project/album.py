from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        elif song in self.songs:
            return "Song is already in the album."

        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        else:
            for s in self.songs:
                if s.name == song_name:
                    self.songs.remove(s)
                    return f"Removed song {song_name} from album {self.name}."

            else:
                return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self) -> str:
        current_songs = []
        for s in self.songs:
            current_songs.append(s.get_info())
        current_songs = "\n".join([f"== {information}" for information in current_songs])
        return f"Album {self.name}\n" \
               f"{current_songs}"
