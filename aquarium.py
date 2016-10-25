from guppy import Guppy
from operator import attrgetter


def experiment(life_time):
    guppy_list = list()

    max_number_of_guppies = 10
    current_number_of_food = max_number_of_guppies * 10
    current_food_eaten = 0

    for i in range(max_number_of_guppies):
        guppy_list.append(Guppy())

    for day in range(life_time):
        for guppy in guppy_list:
            if guppy.spend_a_day():
                current_number_of_food -= 1
                current_food_eaten += 1

                # every time 10 pieces were eaten weakest guppy has to die
                if (current_food_eaten % 10) == 0:
                    print current_food_eaten
                    weakest_guppy = min(guppy_list, key=attrgetter('points'))
                    print "{} had to die. Sorry!".format(weakest_guppy)
                    guppy_list.remove(weakest_guppy)
                    # IDEA: Log the ranking every time this happens


    print "Survivors: {}".format(guppy_list)

if __name__ == "__main__":
    experiment(50)
