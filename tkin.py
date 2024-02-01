from tkinter import *
import warnings


class tkinError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__mes  = message
    def __str__(self):
        return f'Error: {self.__mes}'

class tkinWarning(Warning):
    def __init__(self, warnins):
        self.__warn = warnins
        super().__init__()
    def __str__(self):
        return f'warning {self.__warn}'