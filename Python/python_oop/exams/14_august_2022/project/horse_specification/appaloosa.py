from project.horse_specification.horse import Horse

class Appaloosa(Horse):
    MAX_SPEED = 120

    def train(self):
        self.speed = min(self.speed + 2, self.MAX_SPEED)
        # self.speed += 2
        # if self.speed > self.MAX_SPEED:
        #     self.speed = self.MAX_SPEED