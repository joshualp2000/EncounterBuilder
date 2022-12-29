from random import randint

from Encounter import Encounter
from Party import Party
from Monster import Monster
from Tables import *

def main():
    # party = read_party()
    # monsters = read_monsters("Monsters/" + input("Enter filename for monsters: "))
    party = Party(count=6, level=5)
    monsters = read_monsters("Monsters/Canyon")
    gen_encounters(party, monsters)



def read_party():
    return Party(count=int(input("How many players?")), level=int(input("What level? ")))

def read_monsters(filename):
    monsters = []
    f = open(filename, "r")
    for line in f:
        data = line.split(",")
        if len(data) != 4: continue
        monsters.append(
            Monster(
                name=data[0],
                exp=int(data[1]),
                min=0 if not data[2].strip().isnumeric() else int(data[2].strip()),
                p=0 if not data[3].strip().isnumeric() else int(data[3].strip())
            )
        )
    return monsters


def gen_encounters(party, monsters):
    """
    :param party: Used to calculate the xp ranges
    :param monsters: Used to generate potential encounters
    :return:
    """
    ranges = calc_difficulty_ranges(party)

    encounter = Encounter()
    for i, m in enumerate(monsters):
        encounter.add_monster(m)
        encounter.set_count(m.get_min(), i)

    x = get_difficulty(encounter.get_xp(), ranges)
    print(STRING_DIFFICULTIES[x])
    print(encounter)

    while x != len(ranges):
        new_monster_index = gen_next_index(monsters)
        encounter.increment_count(monsters[new_monster_index])
        new_x = get_difficulty(encounter.get_xp(), ranges)
        if new_x != x:
            x = new_x
            print(STRING_DIFFICULTIES[x])
            print(encounter)

def calc_difficulty_ranges(party):
    trivial_max = party.get_count() * DIFFICULTY_XP[party.get_level() - 1][0]
    easy_max = party.get_count() * DIFFICULTY_XP[party.get_level() - 1][1]
    medium_max = party.get_count() * DIFFICULTY_XP[party.get_level() - 1][2]
    hard_max = party.get_count() * DIFFICULTY_XP[party.get_level() - 1][3]
    return [trivial_max, easy_max, medium_max, hard_max]

def get_difficulty(xp, ranges):
    for i in range(len(ranges)):
        if xp < ranges[i]:
            return i
    return len(ranges)

def gen_next_index(monsters):
    n = randint(1, 100)
    r = 0
    for i, m in enumerate(monsters):
        r += m.get_p()
        if n < r:
            # print(n, m.get_name())
            return i
    return randint(0, len(monsters) - 1)


main()