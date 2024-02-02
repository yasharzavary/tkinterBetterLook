from tkinter import *
import os
import warnings
import re
from tkinter import messagebox

class messBog():
    def __init__(self, mes):
        self.__mes = mes

    def makeError(self):
        messagebox.showerror('Error', self.__mes)

    def showInfo(self):
        messagebox.showinfo('Info', self.__mes)


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

    @property
    def getWidgets(self):
        return self.__root.winfo_children()

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


    def __frameControl(self, b, w, h):
        self.__colorChecker(b)
        if (w != None and w <= 0) or (h != None and h <= 0): raise tkinError('your with and height isn\'t valid')

    def __whereChecker(self, where):
        if where not in [LEFT, RIGHT, BOTTOM, TOP, None]:
            raise tkinError('not valid where input')

    def addFrame(self, bg='#526D82', width=None, height=None, where=None, expand=False):
        self.__frameControl(bg, width, height)
        if width is None: width = self.__width // 4
        if height is None: height = self.__height // 4
        frame = Frame(master=self.__root, bg=bg, width=width, height=height)
        frame.pack_propagate(False)
        if where is None: frame.pack(expand=expand)
        else: frame.pack(side=where, expand=expand)
        return frame

    def __colorChecker(self, b):
        if isinstance(b, list):
            for i in b:
                if not re.search(r'[0-9A-F]', i) or len(i) != 7: raise tkinError('your color info isn\'t valid')
        elif not re.search(r'[0-9A-F]', b) or len(b) != 7: raise tkinError('your background color isn\'t valid')

    def __buttonControl(self, action, doupleAction, bgIn, bg, fg, cursor):
        if not callable(action): raise tkinError('you must give one function in action')
        if doupleAction == None: tkinWarning('your double action not writed...it can make some false actions in your code')
        elif not callable(doupleAction): raise tkinError('you must give one function in doubleAction')
        self.__colorChecker([bgIn, bg, fg])

    def  addButton(self, action, doubleAction=None, master=None, bgIn='#DDE6ED', bg='#9DB2BF', fg='#000000', text = 'click', cursor='fleur', where = None):
        self.__buttonControl(action, doubleAction, bgIn, bg, fg, cursor)
        but = Button(master=master if  master != None else self.__root, text=text, bg=bg, cursor=cursor, fg=fg)
        but.bind('<Button>', action)
        but.bind('<Enter>', lambda x: but.config(bg=bgIn))
        but.bind('<Leave>', lambda x: but.config(bg=bg))
        self.__whereChecker(where)
        if where is None: but.pack()
        else: but.pack(side=where)
        return but
    def addEntry(self, master=None, where=RIGHT):
        ent = Entry(master=master if master != None else self.__root)
        self.__whereChecker(where)
        ent.pack(side=where)
        return ent


    def addText(self, text='', master=None, where=None, bg=None, fg='#000000'):
        t = Label(master=master if master != None else self.__root, text=text, fg=fg, bg=self.__bg if bg ==None else bg)
        self.__whereChecker(where)
        if where is None: t.pack()
        else: t.pack(side=where)

    def __del__(self):
        try:
            self.__root.destroy()
        except:
            pass