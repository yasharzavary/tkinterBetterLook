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


class window():
    def __init__(self, title='window', w=500, h=500, x=0, y=0, iconAddress=None, bgColor = '#526D82'):
        self.__root = None
        self.__bg = '#526D82'
        self.__butBg = '#9DB2BF'
        self.__butBgI = '#DDE6ED'
        self.__width = w
        self.__height = h
        self.__title = title