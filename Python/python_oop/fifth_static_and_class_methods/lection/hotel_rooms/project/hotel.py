from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None or str:
        room_after = ""
        for r in self.rooms:
            if r.number == room_number:
                room_after = r.take_room(people)
                break

        if isinstance(room_after, str):
            return room_after
        else:
            self.guests += people

    def free_room(self, room_number: int) -> None or str:
        freed_room = ""
        for r in self.rooms:
            if r.number == room_number:
                self.guests -= r.guests
                freed_room = r.free_room()
                break

        if isinstance(freed_room, str):
            return freed_room

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
