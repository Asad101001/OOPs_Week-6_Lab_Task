import tkinter as tk
from Point import Point
from Pen import Pen
from Canvas import TKPanel
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Asad's Drawing Canvas")
        self.canvas = TKPanel(self.root, width = 1000 , height = 1000)
        self.canvas.pack()

    def run( self ):

    ##Point##
        A = Point()
        B = Point (6, 9)
        print("Point B's original values of x:",B.get_x() , " and y:", B.get_y())
        B.set_x(7)
        B.set_y(11)
        C = Point(B)
        D = Point(4,1)
        E = C.__add__(D)
        print("Point B's altered values of x:",B.__str__())
        print("Point E = A + C : ", E)

##Canvas window display with lines drawn by Pen##
        pen = Pen (self.canvas)

        #Making an 'A' (coordinates figured out using ChatGPT)
        pen.move_to (150, 500)
        pen.line_to (200, 400)
        pen.line_to (250, 500)
        pen.move_to (175, 450)
        pen.line_to (225, 450)

        self.root.mainloop ()


