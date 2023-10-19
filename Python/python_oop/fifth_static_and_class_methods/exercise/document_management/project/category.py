class Category:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {str(self.id)}: {self.name}"
