import names
import random

class Guppy:

    def __init__(self, parent_id=None, last_name=None):
        self.id = random.randint(10000, 99999)
        self.first_name = names.get_first_name()
        self.last_name = last_name
        if not self.last_name:
            self.last_name = names.get_last_name()

        self.points = 1
        self.children = list()
        self.alive = True

    def eat(self):
        self.points += 1

    def get_children(self):
        child_guppy = Guppy()
        self.children.append(child_guppy)

    def spend_a_day(self):
        # randomize True, False
        if bool(random.getrandbits(1)):
            self.points += 1
            return True
        else:
            return False

    def __repr__(self):
        return "{} {}: {} Points".format(self.first_name, self.last_name, self.points)
