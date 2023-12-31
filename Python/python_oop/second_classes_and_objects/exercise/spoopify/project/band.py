from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."

                else:
                    self.albums.remove(a)
                    return f"Album {album_name} has been removed."

        else:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        current_albums = []
        for al in self.albums:
            current_albums.append(al.details())
        current_albums = "\n".join(current_albums)
        return f"Band {self.name}\n" \
               f"{current_albums}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())

album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)

print(album.add_song(second_song))
print(album.details())
print(album.publish())

band = Band("Manuel")

print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
