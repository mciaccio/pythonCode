#!/usr/bin/env python3.5

# import the turtle file (lowercase "t") file from the Python Standard Library
import turtle

window = turtle.Screen()

# print ("\nHello World!\n")

def draw_square():
    print ("\tBegin draw_square function\n")

    # opens a window
    # window = turtle.Screen()
    window.bgcolor("red")

    # get / echo the background color - note could not find getter method
    # print(window.bgcolor())
    print ("\twindow.bgcolor() is %s" % window.bgcolor())


    # get the class of the window object
    print ("\twindow.__class__ is %s" % window.__class__)
    # window.__class__ is <class 'turtle._Screen'>

    # get the class name of the window object
    print ("\twindow.__class__.__name__ is %s\n" % window.__class__.__name__)
    # window.__class__.__name__ is _Screen

    # get the class methods 
    # print ("\tdir (window.__class__) is -> %s\n" % dir (window.__class__))
 
    # dir (window.__class__) is -> ['_RUNNING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    # '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '
    # __repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bgcolor', '_blankimage', '_canvas', '_color',
    # '_colorstr', '_createimage', '_createline', '_createpoly', '_delay', '_delete', '_destroy', '_drawimage', '_drawline', '_drawpoly', '_image',
    # '_incrementudc', '_iscolorstring', '_listen', '_onclick', '_ondrag', '_onkeypress', '_onkeyrelease', '_onrelease', '_onscreenclick',
    # '_ontimer', '_pointlist', '_rescale', '_resize', '_root', '_setbgpic', '_setscrollregion', '_title', '_type', '_update', '_window_size',
    # '_write', 'addshape', 'bgcolor', 'bgpic', 'bye', 'clear', 'clearscreen', 'colormode', 'delay', 'exitonclick', 'getcanvas', 'getshapes',
    # 'listen', 'mainloop', 'mode', 'numinput', 'onclick', 'onkey', 'onkeypress', 'onkeyrelease', 'onscreenclick', 'ontimer', 'register_shape',
    # 'reset', 'resetscreen', 'screensize', 'setup', 'setworldcoordinates', 'textinput', 'title', 'tracer', 'turtles',
    # 'update', 'window_height', 'window_width']
 
    # get the methods of the class
    # print(dir(turtle))
    # ['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle',
    # 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__',
    #  '__builtins__', '__cached__', '__doc__', '__file__', '__forwardmethods', '__func_body', '__loader__', '__methodDict', '__methods',
    #  '__name__', '__package__', '__spec__', '__stringBody', '_alias_list', '_make_global_funcs', '_screen_docrevise', '_tg_classes',
    # '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'addshape', 'back', 'backward',
    # 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone',
    # 'color', 'colormode', 'config_dict', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick',
    # 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle',
    # 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop',
    # 'math', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd',
    # 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape',
    # 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle',
    # 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle',
    # 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles',
    # 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write',
    # 'write_docstringdict', 'xcor', 'ycor']

    # instantiate the Turtle class uppercase "T"
    # located in turtle file lowercase "t"
    # imported from the Python Standard Library 
    brad = turtle.Turtle()
    #__init__ method of the Turtle class called here 
    
    # print ("\tbrad.__class__ is %s" % brad.__class__)
    print('\tbrad.__class__ is -> {}'.format(brad.__class__))
    # print ("\tbrad.__class__.__name__ is %s" % brad.__class__.__name__)
    print('\tbrad.__class__.__name__ is -> {}\n'.format(brad.__class__.__name__))

    brad.shape("square")
    brad.color("yellow")
    brad.speed(0)

    # window.exitonclick()


    for outer in range(0, 60):
        for x in range(0, 4):
            # print ("\tx is %d" % (x))
            brad.forward(100)
            brad.right(90)
        # print(outer)
        # brad.setheading(outer)
        # brad.forward(outer)
        # brad.setx(outer)
        # brad.sety(outer)
        brad.right(6)


    # window.exitonclick()
    
    print ("\tEnd draw_square function\n")

def draw_circle():
    print ("\tBegin draw_circle function\n")

    window.bgcolor("green")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(10)
    angie.circle(100)
    
    print ("\tEnd draw_circle function\n")

def draw_triangle():
    print ("\tBegin draw_triangle function\n")

    window.bgcolor("white")

    triDraw = turtle.Turtle()
    triDraw.shape("arrow")
    triDraw.color("green")
    triDraw.speed(10)
    triDraw.forward(100)
    triDraw.right(120)
    triDraw.forward(100)
    triDraw.right(120)
    triDraw.forward(100)

    print ("\tEnd draw_triangle function\n")
    

def close_out_window():
    print ("\tBegin close_out_window function\n")

    window.exitonclick()

    print ("\tEnd close_out_window function\n")
    

print ("\nBegin mindstorms.py python module \n")

draw_square()

# draw_circle()
# draw_triangle()
close_out_window()

print ("End mindstorms.py python module \n")

