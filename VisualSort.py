from tkinter import *
from tkinter import ttk
import tkinter
import random
import time
import queue

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
quick_time = 0

# number of algorithms in place
alg_num = 6

# window
window = Tk()
window.title("Visual Sort")

# layout intended for task bar on the left-hand side of the screen
# consider full screen implementation
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
    coordinates_list.clear()
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


def launch_test():
    test_page = Tk()
    test_page.title("Test")
    test_page.geometry('533x262+575+348')

    q = queue.Queue(maxsize=3)

    iteration_list = [0, 0, 0]
    comparison_list = [0, 0, 0]
    time_elapsed_list = [0, 0, 0]

    # apply values and data to
    # each of the three labels
    def update_labels():
        cont = 2
        for element in list(q.queue):
            label_list[cont].configure(text=element + '\n' + str(iteration_list[cont]) + '\n' +
                                            str(comparison_list[cont]) + '\n' +
                                            str(round(time_elapsed_list[cont], 3)) + 's')
            print(iteration_list)
            cont -= 1

    def label(x):
        idx = x
        if q.qsize() <= 2:
            q.put(buttons_test_list[idx])
        elif q.qsize() >= 3:
            while q.qsize() > 2:
                q.get()
            q.put(buttons_test_list[idx])
        print(q.qsize())
        update_labels()

    # define checkboxes
    bubble_btn = Button(test_page, text='Bubble Sort', command=lambda: label(1))
    insertion_btn = Button(test_page, text='Insertion Sort', command=lambda: label(2))
    selection_btn = Button(test_page, text='Selection Sort', command=lambda: label(3))
    quick_btn = Button(test_page, text='Quick Sort', command=lambda: label(4))
    heap_btn = Button(test_page, text='Heap Sort', command=lambda: label(5))
    shell_btn = Button(test_page, text='Shell Sort', command=lambda: label(6))

    # button list
    btn_list = [bubble_btn, insertion_btn, selection_btn, quick_btn, heap_btn, shell_btn]

    # place checkboxes
    y_prime_prime = 64
    for btn in range(len(btn_list)):
        btn_list[btn].place(x=48, y=y_prime_prime)
        y_prime_prime += 32

    # three labels
    label_one = Label(test_page)
    label_two = Label(test_page)
    label_three = Label(test_page)

    # label list
    label_list = [label_one, label_two, label_three]

    lbl_k = 100
    for lbl in range(len(label_list)):
        label_list[lbl].place(x=200 + (lbl_k * lbl), y=96)

    # code runs on when run button is pressed ...
    # for each algorithm in the queue, the corresponding stats
    # are projected under their respective labels
    def run():
        global coordinates_list
        # create_visual()
        s.set(launch_s.get())
        index_val = []
        for element in list(q.queue):
            for bll in range(len(buttons_test_list)):
                if str(element) == buttons_test_list[bll]:
                    index_val.append(bll)
        print(index_val)
        new_cl = coordinates_list
        for value in range(len(index_val)):
            coordinates_list = new_cl
            components[value].invoke()
            comparison_list[value] = compare
            iteration_list[value] = iterate
            time_elapsed_list[value] = elapse_rt
        update_labels()

    # components in launch_test window
    instruct_label = Label(test_page, text='Choose Three Algorithms:')
    run_btn = Button(test_page, text='Run', command=run)
    launch_s = Scale(test_page, orient=HORIZONTAL, length=125, from_=c, to=d)
    launch_s.place(x=300, y=16)

    # layout for launch_test_windows
    run_btn.place(x=450, y=32)
    instruct_label.place(x=48, y=36)

    # buttons test list
    buttons_test_list = ['null', 'Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort', 'Heap Sort',
                         'Shell Sort']

    # mainloop
    test_page.mainloop()


# methods
def update_comparisons():
    comparisons.configure(text='Comparisons:\t' + str(compare))


def update_iterations():
    iterations.configure(text='Iterations:\t' + str(iterate))


def update_elapsed():
    elapsed.configure(text='Time Elapsed:\t' + str(round(elapse_rt, 3)) + 's')


def stop():
    coordinates_list.clear()
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


def print_rectangles(val1, val2):
    for index in range(s.get()):
        if index == val1 or index == val2:
            canvas.create_rectangle(coordinates_list[index], fill='red')
        else:
            canvas.create_rectangle(coordinates_list[index], fill='black')


def print_final():
    clear()
    for index in range(s.get()):
        canvas.create_rectangle(coordinates_list[index], fill='green')


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
                print_rectangles(rectangle - 1, rectangle)
                canvas.update()
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()
    print_final()


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
                print_rectangles(minimum, selection_i)
                canvas.update()
            selection_i += 1
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()
        minimum += 1
    print_final()


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
            print_rectangles(pos, pos - 1)
            canvas.update()
            end_time = time.time() - start_time
            elapse_rt = end_time
            update_elapsed()
        coordinates_list[pos] = cursor
    print_final()


def partition(low, high):
    global elapse_rt
    global compare
    global iterate
    idx = (low - 1)
    pivot = coordinates_list[high]
    for rectangle in range(low, high):
        iterate += 1
        update_iterations()
        print(coordinates_list[rectangle])
        if coordinates_list[rectangle][3] <= pivot[3]:
            compare += 1
            update_comparisons()
            idx += 1
            swap(idx, rectangle)
            clear()
            print_rectangles(idx, rectangle)
            canvas.update()
            end_time = time.time() - quick_time
            elapse_rt = end_time
            update_elapsed()
    swap(idx + 1, high)
    return idx + 1


def quick_sort(low, high):
    if low < high:
        pi = partition(low, high)
        quick_sort(low, pi - 1)
        quick_sort(pi + 1, high)
    if low == high:
        print_final()


def quick():
    global quick_time
    global compare
    compare = 0
    global iterate
    iterate = 0
    quick_time = time.time()
    quick_sort(0, len(coordinates_list) - 1)


def heapify(n, index):
    global compare
    largest = index
    var_l = 2 * index + 1
    var_r = 2 * index + 2
    if var_l < n and coordinates_list[index][3] < coordinates_list[var_l][3]:
        largest = var_l
        compare += 1
        update_comparisons()
    if var_r < n and coordinates_list[largest][3] < coordinates_list[var_r][3]:
        compare += 1
        update_comparisons()
        largest = var_r
    if largest != index:
        swap(index, largest)
        clear()
        print_rectangles(index, largest)
        canvas.update()
        heapify(n, largest)


def heap():
    global elapse_rt
    start_time = time.time()
    global compare
    compare = 0
    global iterate
    iterate = 0
    n = len(coordinates_list)
    for rectangle in range(n, -1, -1):
        end_time = time.time() - start_time
        elapse_rt = end_time
        update_elapsed()
        iterate += 1
        update_iterations()
        heapify(n, rectangle)
    for next_rectangle in range(n - 1, 0, -1):
        end_time = time.time() - start_time
        elapse_rt = end_time
        update_elapsed()
        iterate += 1
        update_iterations()
        swap(next_rectangle, 0)
        clear()
        print_rectangles(next_rectangle, 0)
        canvas.update()
        heapify(next_rectangle, 0)
    print_final()


def shell():
    global elapse_rt
    start_time = time.time()
    global compare
    compare = 0
    global iterate
    iterate = 0
    n = int(len(coordinates_list))
    gap = int(n / 2)
    while gap > 0:
        for rectangle in range(int(gap), int(n)):
            iterate += 1
            update_iterations()
            temp = coordinates_list[rectangle]
            j = rectangle
            while j >= int(gap) and coordinates_list[j - int(gap)][3] > temp[3]:
                compare += 1
                update_comparisons()
                swap(j, j - int(gap))
                clear()
                print_rectangles(j, j - int(gap))
                canvas.update()
                j -= int(gap)
                end_time = time.time() - start_time
                elapse_rt = end_time
                update_elapsed()
            coordinates_list[j] = temp
        gap = gap / 2
    print_final()


# scale with values from c to d
s = Scale(window, orient=HORIZONTAL, length=250, from_=c, to=d)
s.place(x=50, y=50)

# buttons
create_visual = Button(window, text='Create Visual', command=create)
bubble_sort_button = Button(window, text='Bubble Sort', command=bubble)
selection_sort_button = Button(window, text='Selection Sort', command=selection)
insertion_sort_button = Button(window, text='Insertion Sort', command=insertion)
quick_sort_button = Button(window, text='Quick Sort', command=quick)
heap_sort_button = Button(window, text='Heap Sort', command=heap)
shell_sort_button = Button(window, text='Shell Sort', command=shell)
clear_button = Button(window, text='Clear', command=stop)
test_button = Button(window, text='Test', command=launch_test)

# placement
# components is order-sensitive
components = [create_visual, bubble_sort_button, selection_sort_button, insertion_sort_button, quick_sort_button,
              heap_sort_button, shell_sort_button, clear_button, test_button, comparisons, iterations, elapsed]

comp_text = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Heap Sort', 'Shell Sort']

y_prime = 115
for comp in components:
    comp.place(x=50, y=y_prime)
    y_prime += 50

# mainloop
window.mainloop()
