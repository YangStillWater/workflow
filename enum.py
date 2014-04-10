__author__ = 'Peng'


class Enum(tuple): __getattr__ = tuple.index
