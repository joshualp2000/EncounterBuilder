class Party:
    def __init__(self, count, level):
        self.__count = count
        self.__level = level

    def get_count(self):
        return self.__count

    def get_level(self):
        return self.__level