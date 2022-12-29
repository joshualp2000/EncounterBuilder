class Monster:
    def __init__(self, name, exp, min, p):
        self.__name = name
        self.__exp = exp
        self.__min = min
        self.__p = p

    def get_name(self):
        return self.__name

    def get_exp(self):
        return self.__exp

    def get_min(self):
        return self.__min

    def get_p(self):
        return self.__p

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_exp() == other.get_exp()

    def __repr__(self):
        return self.__name
