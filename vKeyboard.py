"""
vKeyboard - an on-screen keyboard optimized for small screens (e.g. PiTFT)

Copyright (C) 2016  Fantilein1990

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

created on 2016-08-03
last changed on 2016-09-07 - version 1.0

vKeyboard is based upon tkinter-keyboard by petemojeiko
(https://github.com/petemojeiko/tkinter-keyboard/blob/master/keyboard.py)
"""

import Tkinter as tk
import ttk

# -- Declaration of font styles --- #
font_title = ("Helvetica", 18, "bold")
font_message = ("Helvetica", 14)
font_message_small = ("Helvetica", 11)
font_vKeyboard = ("Helvetica", 10)
font_vKeyboardSpecialKeys = ("Helvetica", 10, "bold")

# -- GUI's main class -- #
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self, width=480, height=320)
        container.grid_propagate(0)
        container.pack(fill="both", expand=1)

        ttk.Style().configure("vKeyboard.TButton", font=font_vKeyboard)
        ttk.Style().configure("vKeyboardSpecial.TButton", font=font_vKeyboardSpecialKeys)

        self.frames = {}

        for F in (StartPage, SecondPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("StartPage")

    def showFrame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text="Example Page", font=font_title)
        label1.pack(side="top", fill="x", pady=7, padx=10)

        self.label1 = ttk.Label(self, text="Enter something:", font=font_message)
        self.label1.pack(side="top")
        self.entry1 = ttk.Entry(self)
        self.entry1.pack(side="top")

        self.label0 = ttk.Label(self, text="  ", font=font_message)
        self.label0.pack(side="top")
        self.label2 = ttk.Label(self, text="Enter something else:", font=font_message)
        self.label2.pack(side="top")
        self.entry2 = ttk.Entry(self)
        self.entry2.pack(side="top")

        self.frame1 = ttk.Frame(self, width=480, height=280)
        self.frame1.pack(side="top", pady=30)
        self.frame2 = ttk.Frame(self, width=480, height=280)
        self.frame2.pack(side="top", pady=30)

        self.keysize = 4
        self.controller = controller
        self.enterAction = "StartPage"

        self.entry1.bind("<FocusIn>", lambda e:  self.show_vKeyboard(1))
        self.entry2.bind("<FocusIn>", lambda e:  self.show_vKeyboard(2))

        self.kb = vKeyboard(attach=self.entry1,
                            x=self.entry1.winfo_rootx(),
                            y=self.entry1.winfo_rooty() + self.entry1.winfo_reqheight(),
                            keysize=self.keysize,
                            parent=self.frame1,
                            controller=self.controller,
                            enterAction=self.enterAction)

    def show_vKeyboard(self, k):
        if k == 1:
            self.frame1.destroy()
            self.frame2.destroy()
            self.kb.destroy()

            self.frame1 = ttk.Frame(self, width=480, height=280)
            self.frame1.pack(side="top", pady=30)
            self.kb = vKeyboard(attach=self.entry1,
                                 x=self.entry1.winfo_rootx(),
                                 y=self.entry1.winfo_rooty() + self.entry1.winfo_reqheight(),
                                 keysize=self.keysize,
                                 parent=self.frame1,
                                 controller=self.controller,
                                 enterAction=self.enterAction)

        elif k == 2:
            self.frame1.destroy()
            self.frame2.destroy()
            self.kb.destroy()

            self.frame2 = ttk.Frame(self, width=480, height=280)
            self.frame2.pack(side="top", pady=30)
            self.kb = vKeyboard(attach=self.entry2,
                                 x=self.entry2.winfo_rootx(),
                                 y=self.entry2.winfo_rooty() + self.entry2.winfo_reqheight(),
                                 keysize=self.keysize,
                                 parent=self.frame2,
                                 controller=self.controller,
                                 enterAction=self.enterAction)

class SecondPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text="Example Page 2", font=font_title)
        label1.pack(side="top", fill="x", pady=7, padx=10)

class vKeyboard(ttk.Frame):
    # --- A frame for the keyboard(s) itself --- #
    def __init__(self, parent, attach, x, y, keysize, controller, enterAction):
        ttk.Frame.__init__(self, takefocus=0)

        self.attach = attach
        self.keysize = keysize
        self.parent = parent
        self.x = x
        self.y = y
        self.controller = controller
        self.enterAction = enterAction

    # --- Different sub-keyboards (e.g. alphabet, symbols..) --- #
        # --- Lowercase alphabet sub-keyboard --- #
        self.alpha_Frame = ttk.Frame(parent)
        self.alpha_Frame.grid(row=0, column=0, sticky="nsew")

        self.row1_alpha = ttk.Frame(self.alpha_Frame)
        self.row2_alpha = ttk.Frame(self.alpha_Frame)
        self.row3_alpha = ttk.Frame(self.alpha_Frame)
        self.row4_alpha = ttk.Frame(self.alpha_Frame)

        self.row1_alpha.grid(row=1)
        self.row2_alpha.grid(row=2)
        self.row3_alpha.grid(row=3)
        self.row4_alpha.grid(row=4)

        # --- Uppercase alphabet sub-keyboard --- #
        self.Alpha_Frame = ttk.Frame(parent)
        self.Alpha_Frame.grid(row=0, column=0, sticky="nsew")

        self.row1_Alpha = ttk.Frame(self.Alpha_Frame)
        self.row2_Alpha = ttk.Frame(self.Alpha_Frame)
        self.row3_Alpha = ttk.Frame(self.Alpha_Frame)
        self.row4_Alpha = ttk.Frame(self.Alpha_Frame)

        self.row1_Alpha.grid(row=1)
        self.row2_Alpha.grid(row=2)
        self.row3_Alpha.grid(row=3)
        self.row4_Alpha.grid(row=4)

        # --- Symbols and numerals sub-keyboard --- #
        self.Symbol_Frame = ttk.Frame(parent)
        self.Symbol_Frame.grid(row=0, column=0, sticky="nsew")

        self.row1_Symbol = ttk.Frame(self.Symbol_Frame)
        self.row2_Symbol = ttk.Frame(self.Symbol_Frame)
        self.row3_Symbol = ttk.Frame(self.Symbol_Frame)
        self.row4_Symbol = ttk.Frame(self.Symbol_Frame)

        self.row1_Symbol.grid(row=1)
        self.row2_Symbol.grid(row=2)
        self.row3_Symbol.grid(row=3)
        self.row4_Symbol.grid(row=4)

        # --- Initialize all sub-keyboards --- #
        self.keyState = 1
        self.init_keys()

        self.alpha_Frame.tkraise()

        self.pack()

    def init_keys(self):
        self.alpha = {
            'row1': ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Bksp'],
            'row2': ['Sym', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            'row3': ['ABC', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'ENTER'],
            'row4': ['<<<', '[ space ]', '>>>', 'BACK']
        }
        self.Alpha = {
            'row1': ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Bksp'],
            'row2': ['Sym', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            'row3': ['abc', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'ENTER'],
            'row4': ['<<<', '[ space ]', '>>>', 'BACK']
        }
        self.Symbol = {
            'row1': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Bksp'],
            'row2': ['abc', '!', '"', '$', '%', '&', '/', '(', ')', '[', ']', '='],
            'row3': ['@', '-', '_', '?', '#', '*', '{', '}', ':', ';', 'ENTER'],
            'row4': ['<<<','+', '[ space ]', '.', ',', '>>>', 'BACK']
        }

        for i in range(1, 4):
            if i == 1:
                self.keyStyle = self.alpha
                self.row1 = self.row1_alpha
                self.row2 = self.row2_alpha
                self.row3 = self.row3_alpha
                self.row4 = self.row4_alpha
            elif i == 2:
                self.keyStyle = self.Alpha
                self.row1 = self.row1_Alpha
                self.row2 = self.row2_Alpha
                self.row3 = self.row3_Alpha
                self.row4 = self.row4_Alpha
            elif i == 3:
                self.keyStyle = self.Symbol
                self.row1 = self.row1_Symbol
                self.row2 = self.row2_Symbol
                self.row3 = self.row3_Symbol
                self.row4 = self.row4_Symbol

            for row in self.keyStyle.iterkeys():  # iterate over dictionary of rows
                if row == 'row1':  # TO-DO: re-write this method
                    i = 1  # for readability and functionality
                    for k in self.keyStyle[row]:
                        if k == 'Bksp':
                            ttk.Button(self.row1,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 2,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        else:
                            ttk.Button(self.row1,
                                       style="vKeyboard.TButton",
                                       text=k,
                                       width=self.keysize,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        i += 1
                elif row == 'row2':
                    i = 2
                    for k in self.keyStyle[row]:
                        if k == 'Sym':
                            ttk.Button(self.row2,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 1.5,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        elif k == 'abc':
                            ttk.Button(self.row2,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 1.5,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        else:
                            ttk.Button(self.row2,
                                       style="vKeyboard.TButton",
                                       text=k,
                                       width=self.keysize,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        i += 1
                elif row == 'row3':
                    i = 2
                    for k in self.keyStyle[row]:
                        if k == 'ABC':
                            ttk.Button(self.row3,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 1.5,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        elif k == 'abc':
                            ttk.Button(self.row3,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 1.5,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        elif k == 'ENTER':
                            ttk.Button(self.row3,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 2.5,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        else:
                            ttk.Button(self.row3,
                                       style="vKeyboard.TButton",
                                       text=k,
                                       width=self.keysize,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        i += 1
                else:
                    i = 3
                    for k in self.keyStyle[row]:
                        if k == '[ space ]':
                            ttk.Button(self.row4,
                                       style="vKeyboard.TButton",
                                       text='     ',
                                       width=self.keysize * 6,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        elif k == 'BACK':
                            ttk.Button(self.row4,
                                       style="vKeyboardSpecial.TButton",
                                       text=k,
                                       width=self.keysize * 2,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        else:
                            ttk.Button(self.row4,
                                       style="vKeyboard.TButton",
                                       text=k,
                                       width=self.keysize,
                                       command=lambda k=k: self._attach_key_press(k)).grid(row=0, column=i)
                        i += 1

    def _attach_key_press(self, k):
        if k == '>>>':
            self.attach.tk_focusNext().focus_set()
        elif k == '<<<':
            self.attach.tk_focusPrev().focus_set()
        elif k == 'Sym':
            self.Symbol_Frame.tkraise()
        elif k == 'abc':
            self.alpha_Frame.tkraise()
        elif k == 'ABC':
            self.Alpha_Frame.tkraise()
        elif k == 'Bksp':
            self.remaining = self.attach.get()[:-1]
            self.attach.delete(0, tk.END)
            self.attach.insert(0, self.remaining)
        elif k == 'ENTER':
            pass                                    # Define, what's supposed to happen..
            #self.controller.enter_cb(self.enterAction)
        elif k == 'BACK':
            self.controller.showFrame("StartPage")  # Or any other page...
        elif k == '[ space ]':
            self.attach.insert(tk.END, ' ')
        else:
            self.attach.insert(tk.END, k)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
