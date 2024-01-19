class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        new_date = date.split(".")
        month = new_date[1]
        year = int(new_date[2])
        list_of_months = {'1': 'January', '2': 'February', '3': 'March',
                          '4': 'April', '5': 'May', '6': 'June', '7': 'July',
                          '8': 'August', '9': 'September', '10': 'October',
                          '11': 'November', '12': 'December'}
        month_str = list_of_months[month]

        return cls(name, id, year, month_str, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} " \
               f"({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
