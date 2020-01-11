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


def launch_test():
    test_page = Tk()
    test_page.title("Test")
    test_page.geometry('463x262+575+348')

    # check buttons
    bubble_var = IntVar()
    check_bubble = Checkbutton(test_page, text='Bubble Sort', variable=bubble_var)
    check_bubble.pack()
    insertion_var = IntVar()
    check_insertion = Checkbutton(test_page, text='Insertion Sort', variable=insertion_var)
    check_insertion.pack()
    selection_var = IntVar()
    check_selection = Checkbutton(test_page, text='Selection Sort', variable=selection_var)
    check_selection.pack()
    quick_var = IntVar()
    check_quick = Checkbutton(test_page, text='Quick Sort', variable=quick_var)
    check_quick.pack()
    heap_var = IntVar()
    check_heap = Checkbutton(test_page, text='Heap Sort', variable=heap_var)
    check_heap.pack()
    shell_var = IntVar()
    check_shell = Checkbutton(test_page, text='Shell Sort', variable=shell_var)
    check_shell.pack()

    def run():
        check_button_list = [bubble_var.get(), insertion_var.get(), selection_var.get(), quick_var.get(),
                             heap_var.get(), shell_var.get()]
        check_sum = 0
        for variables in range(alg_num):
            check_sum += check_button_list[variables]
        print(check_sum)

    # components in launch_test window
    instruct_label = Label(test_page, text='Choose Up to Three Algorithms:')
    run_btn = Button(test_page, text='Run', command=run)
    launch_s = Scale(test_page, orient=HORIZONTAL, length=125, from_=c, to=d)
    launch_s.place(x=300, y=16)

    # layout for launch_test_windows
    run_btn.place(x=400, y=72)
    instruct_label.place(x=48, y=36)
    check_bubble.place(x=48, y=72)
    check_insertion.place(x=48, y=96)
    check_selection.place(x=48, y=120)
    check_quick.place(x=48, y=144)
    check_heap.place(x=48, y=168)
    check_shell.place(x=48, y=192)

    # mainloop
    test_page.mainloop()


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
create_visual.place(x=50, y=115)
bubble_sort_button.place(x=50, y=165)
selection_sort_button.place(x=50, y=215)
insertion_sort_button.place(x=50, y=265)
quick_sort_button.place(x=50, y=315)
heap_sort_button.place(x=50, y=365)
shell_sort_button.place(x=50, y=415)
clear_button.place(x=50, y=465)
test_button.place(x=50, y=515)
comparisons.place(x=50, y=815)
iterations.place(x=50, y=840)
elapsed.place(x=50, y=865)

# mainloop
window.mainloop()
