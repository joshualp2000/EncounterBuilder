class Encounter:
    def __init__(self):
        self.__monsters = []
        self.__counts = []

    def get_monsters(self):
        return self.__monsters

    def get_counts(self):
        return self.__counts

    def get_xp(self):
        xp = 0
        total_monsters = 0
        for i in range(len(self.__monsters)):
            xp += self.__monsters[i].get_exp() * self.__counts[i]
            total_monsters += self.__counts[i]
        if total_monsters < 2:
            multiplier = 1
        elif total_monsters < 3:
            multiplier = 1.5
        elif total_monsters < 7:
            multiplier = 2
        elif total_monsters < 11:
            multiplier = 2.5
        elif total_monsters < 15:
            multiplier = 3
        else:
            multiplier = 4
        return xp * multiplier

    def set_count(self, new_val, i):
        self.__counts[i] = new_val

    def increment_count(self, monster):
        for i, m in enumerate(self.__monsters):
            if m == monster:
                self.__counts[i] += 1

    def add_monster(self, monster):
        for m in self.__monsters:
            if m == monster:
                return
        self.__monsters.append(monster)
        self.__counts.append(monster.get_min())

    def __repr__(self):
        s = ""
        for i in range(len(self.__monsters)):
            if self.__counts[i] > 0:
                s += str(self.__counts[i]) + " X " + self.__monsters[i].get_name() + "\n"
        return s