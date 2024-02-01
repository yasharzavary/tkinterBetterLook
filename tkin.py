from tkinter import *
import warnings
import os

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
        self.__root = self.__windowMaker(title, w, h, x, y, iconAddress, bgColor)
        self.__bg = '#526D82'
        self.__butBg = '#9DB2BF'
        self.__butBgI = '#DDE6ED'
        self.__width = w
        self.__height = h
        self.__title = title

    def __control(self, w, h, x, y, icon, scrW, scrH):
        """
        control our window information that given it
        :input: window info
        """
        if w <= 0 or h <= 0: raise tkinError('make sure about w and h...they can\'t be zero or under the zero')
        if icon and not os.path.exists(icon): raise tkinError('this isn\'t valid icon address')
        if x < 0 or y < 0 or x > scrW or y > scrH: warnings.warn(tkinWarning('x and y place cordinate out of range...you window will go outside of the screen'))

    def __windowMaker(self, title, w, h, x, y, iconAddress, bg):
        root = Tk()
        # screen info
        windowHeight = root.winfo_screenheight()
        windowWidth = root.winfo_screenwidth()
        # info check
        self.__control(w, h, x, y, iconAddress, windowWidth, windowHeight)
        root.title(title)
        if x == 0 and y == 0:
            x = (windowWidth / 2) - (w / 2)
            y = (windowHeight / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        if iconAddress: root.iconbitmap(iconAddress)
        root.config(bg=bg)
        return root

    def show(self):
        self.__root.mainloop()

    @property
    def bgColor(self):
        return self.__bg

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new):
        self.__title = new
        self.__root.title(new)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height