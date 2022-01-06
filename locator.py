class BaseLocator:
    def __add__(self, other):
        combination = {}
        combination.update(self.__dict__)
        combination.update(other.__dict__)
        new = self.__class__()
        new.__dict__.update(combination)
        return new
