from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from project.jockey import Jockey



class HorseRaceApp:
    VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = [h for h in self.horses if h.name == horse_name]
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_TYPES:
            self.horses.append(self.VALID_TYPES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        already_race = [r for r in self.horse_races if r.race_type == race_type]
        if already_race:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")


        horse = [h for h in self.horses if h.__class__.__name__ == horse_type]
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if horse[-1].is_taken:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey[0].horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey[0].horse = horse[-1]
        horse[-1].is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse[-1].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        race = [r for r in self.horse_races if r.race_type == race_type]
        
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey[0].horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        jockey_already_added = [j for j in race[0].jockeys if j.name == jockey_name]
        if jockey_already_added:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race[0].jockeys.append(jockey[0])
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = [r for r in self.horse_races if r.race_type == race_type]
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race[0].jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        max_speeder: Jockey = None
        for j in race[0].jockeys:
            if not max_speeder:
                max_speeder = j
            else:
                if max_speeder.horse.speed < j.horse.speed:
                    max_speeder = j

        return f"The winner of the {race_type} race, with a speed of {max_speeder.horse.speed}km/h is {max_speeder.name}! Winner's horse: {max_speeder.horse.name}."