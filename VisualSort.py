from tkinter import *
import tkinter
import random
import time

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
s = 0
compare = 0
iterate = 0
elapse_rt = 0

# window
window = Tk()
window.title("Visual Sort")
window.geometry('1852x1049+60+0')

# canvas
canvas = Canvas(window, width=w, height=h)
canvas.place(x=320, y=0)

# labels
comparisons = Label(window, text='Comparisons:\t' + str(compare))
iterations = Label(window, text='Iterations:\t' + str(iterate))
elapsed = Label(window, text='Time Elapsed:\t' + str(elapse_rt) + 's')


# methods
def create():
    global elapse_rt
    elapse_rt = 0
    update_elapsed()
    global iterate
    iterate = 0
    update_iterations()
    global compare
    compare = 0
    update_comparisons()
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


def update_comparisons():
    comparisons.configure(text='Comparisons:\t' + str(compare))


def update_iterations():
    iterations.configure(text='Iterations:\t' + str(iterate))


def update_elapsed():
    elapsed.configure(text='Time Elapsed:\t' + str(elapse_rt) + 's')


def stop():
    global elapse_rt
    elapse_rt = 0
    update_elapsed()
    global iterate
    iterate = 0
    update_iterations()
    global compare
    compare = 0
    update_comparisons()
    canvas.delete('all')


def clear():
    update_iterations()
    update_comparisons()
    canvas.delete('all')


def print_rectangles():
    for index in range(s.get()):
        canvas.create_rectangle(coordinates_list[index], fill='black')


def swap(g, j):
    coordinates_list[g], coordinates_list[j] = coordinates_list[j], coordinates_list[g]
    coordinates_list[g][0], coordinates_list[j][0] = coordinates_list[j][0], coordinates_list[g][0]
    coordinates_list[g][2], coordinates_list[j][2] = coordinates_list[j][2], coordinates_list[g][2]


def bubble():
    global elapse_rt
    global iterate
    global compare
    start_time = time.time()
    n = len(coordinates_list)
    swapped = True
    k = -1
    while swapped:
        iterate += 1
        update_iterations()
        swapped = False
        k = k + 1
        for rectangle in range(1, n - k):
            if coordinates_list[rectangle - 1][3] > coordinates_list[rectangle][3]:
                compare += 1
                update_comparisons()
                swap(rectangle - 1, rectangle)
                swapped = True
                clear()
                print_rectangles()
                canvas.update()
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()


def selection():
    global elapse_rt
    start_time = time.time()
    global iterate
    iterate = 0
    global compare
    minimum = 0
    n = len(coordinates_list)
    while minimum <= (n - 1):
        iterate += 1
        update_iterations()
        selection_i = minimum
        while selection_i <= (n - 1):
            if coordinates_list[selection_i][3] < coordinates_list[minimum][3]:
                compare += 1
                update_comparisons()
                swap(minimum, selection_i)
                clear()
                print_rectangles()
                canvas.update()
            selection_i += 1
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()
        minimum += 1


def insertion():
    global elapse_rt
    start_time = time.time()
    global compare
    compare = 0
    global iterate
    iterate = 0
    for rectangle in range(len(coordinates_list)):
        iterate += 1
        update_iterations()
        cursor = coordinates_list[rectangle]
        pos = rectangle
        while pos > 0 and coordinates_list[pos - 1][3] > cursor[3]:
            compare += 1
            update_comparisons()
            swap(pos, pos - 1)
            pos = pos - 1
            clear()
            print_rectangles()
            canvas.update()
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()
        coordinates_list[pos] = cursor


def heap():
    length = len(coordinates_list)
    least_parent = int(round(length / 2))
    for rectangle in range(least_parent, -1, -1):
        moveDown(i, length)
    for rectangle in range(length, 0, -1):
        if coordinates_list[0][3] > coordinates_list[rectangle][3]:
            swap(0, rectangle)
            moveDown(0, rectangle - 1)


def moveDown(first, last):
    largest = 2 * first + 1
    while largest <= last:
        if largest < last and coordinates_list[largest][3] < coordinates_list[largest + 1][3]:
            largest += 1
        if coordinates_list[largest][3] > coordinates_list[first][3]:
            swap(largest, first)
            first = largest
            largest = 2 * first + 1
        else:
            return


# scale with values from c to d
s = Scale(window, orient=HORIZONTAL, length=250, from_=c, to=d)
s.place(x=50, y=50)

# buttons
create_visual = Button(window, text='Create Visual', command=create)
bubble_sort_button = Button(window, text='Bubble Sort', command=bubble)
selection_sort_button = Button(window, text='Selection Sort', command=selection)
insertion_sort_button = Button(window, text='Insertion Sort', command=insertion)
heap_sort_button = Button(window, text='Heap Sort')
clear_button = Button(window, text='Clear', command=stop)

# placement
create_visual.place(x=50, y=115)
bubble_sort_button.place(x=50, y=165)
selection_sort_button.place(x=50, y=215)
insertion_sort_button.place(x=50, y=265)
heap_sort_button.place(x=50, y=315)
clear_button.place(x=50, y=365)
comparisons.place(x=50, y=815)
iterations.place(x=50, y=840)
elapsed.place(x=50, y=865)

# mainloop
window.mainloop()
