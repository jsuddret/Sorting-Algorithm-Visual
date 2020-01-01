from tkinter import *
import tkinter
import random
import time
import threading

# variables
l = []
coordinates_list = []
a = 89
b = 9001
i = 0
c = 10
d = 750
w = 1512
h = 1044
e = threading.Event()

# window
window = Tk()
window.title("Visual Sort")
window.geometry('1852x1049+60+0')

# canvas
canvas = Canvas(window, width=w, height=h)
canvas.place(x=320, y=0)


# methods
def create():
    coordinates_list.clear()
    clear()
    # create x amount of integer j, min number a, max number b
    l.clear()
    x = s.get()
    y1 = 10
    rectangle_width = w / x
    for index in range(x):
        j = random.randint(a, b)
        l.append(j)  # add to integer list
    for index in range(x):
        rect_x1 = index * rectangle_width
        rect_y1 = y1
        rect_x2 = (index + 1) * rectangle_width
        rect_y2 = l[index] / 9
        canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2,
                                fill='black')
        coordinates = [rect_x1, rect_y1, rect_x2, rect_y2]
        coordinates_list.append(coordinates)


def clear():
    canvas.delete('all')


def print_rectangles():
    for index in range(s.get()):
        canvas.create_rectangle(coordinates_list[index], fill='black')


def swap(g, j):
    coordinates_list[g], coordinates_list[j] = coordinates_list[j], coordinates_list[g]
    coordinates_list[g][0], coordinates_list[j][0] = coordinates_list[j][0], coordinates_list[g][0]
    coordinates_list[g][2], coordinates_list[j][2] = coordinates_list[j][2], coordinates_list[g][2]


def bubble():
    n = len(coordinates_list)
    swapped = True
    k = -1
    while swapped:
        swapped = False
        k = k + 1
        for rectangle in range(1, n - k):
            if coordinates_list[rectangle - 1][3] > coordinates_list[rectangle][3]:
                swap(rectangle - 1, rectangle)
                swapped = True
                clear()
                print_rectangles()
                canvas.update()


def selection():
    for rectangle in range(len(coordinates_list)):
        minimum = rectangle
        for next_rectangle in range(rectangle + 1, len(coordinates_list)):
            if coordinates_list[next_rectangle][3] < coordinates_list[minimum][3]:
                minimum = next_rectangle
            swap(rectangle, minimum)
            clear()
            print_rectangles()
            canvas.update()


def insertion():
    for rectangle in range(len(coordinates_list)):
        cursor = coordinates_list[rectangle]
        pos = rectangle
        while pos > 0 and coordinates_list[pos - 1][3] > cursor[3]:
            swap(pos, pos - 1)
            pos = pos - 1
            clear()
            print_rectangles()
            canvas.update()
        coordinates_list[pos] = cursor


# scale with values from c to d
s = Scale(window, orient=HORIZONTAL, length=250, from_=c, to=d)
s.place(x=50, y=50)

# buttons
create_visual = Button(window, text='Create Visual', command=create)
bubble_sort_button = Button(window, text='Bubble Sort', command=bubble)
selection_sort_button = Button(window, text='Selection Sort', command=selection)
insertion_sort_button = Button(window, text='Insertion Sort', command=insertion)
clear_button = Button(window, text='Clear', command=clear)

# placement
create_visual.place(x=50, y=115)
bubble_sort_button.place(x=50, y=165)
selection_sort_button.place(x=50, y=215)
insertion_sort_button.place(x=50, y=265)
clear_button.place(x=50, y=315)

# mainloop
window.mainloop()
