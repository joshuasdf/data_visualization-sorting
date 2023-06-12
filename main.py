import pygame
from random import shuffle, randint
from time import sleep, perf_counter as pf

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_x, screen_y = screen.get_size()

x = 100
y = screen_y / x

lst = [i for i in range(1, x + 1)]
sorted_lst = [i for i in range(1, x + 1)]
shuffle(lst)

LENGTH = screen_x / x
clock = pygame.time.Clock()

color = (65, 105, 225)
black = (0, 0, 0)

fps = 24


def update_screen():
    events()
    screen.fill(black)
    for index, val in enumerate(lst):
        rect = pygame.Rect(index * LENGTH, 0, LENGTH, val * y)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, black, rect, 1)
    pygame.display.update()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def bubblesort():
    for i in range(x):
        # loop to compare array elements
        for j in range(0, x - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            update_screen()


def insertionsort():
    for i in range(1, x):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        update_screen()
        clock.tick(fps)


def merge(l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = lst[l + i]

    for j in range(0, n2):
        R[j] = lst[m + 1 + j]

    i = 0 
    j = 0  
    k = l  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1


def mergeSort(l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(l, m)
        mergeSort(m + 1, r)
        merge(l, m, r)
        update_screen()
        clock.tick(fps)


def selectionSort():
    for i in range(x):
        min_index = i

        for j in range(i + 1, x):
            if lst[j] < lst[min_index]:
                min_index = j
                
        lst[i], lst[min_index] = lst[min_index], lst[i]
        update_screen()
        clock.tick(fps)


pygame.display.set_caption("Data Visualization")
while True:
    while lst != sorted_lst:
        p = randint(1, 4)
        start = pf()
        if p == 1:
            bubblesort()
            text = "bubble sort"
        elif p == 2:
            insertionsort()
            text = "insertion sort"
        elif p == 3:
            mergeSort(0, x - 1)
            text = "merge sort"
        elif p == 4:
            selectionSort()
            text = "selection sort"

        print("%s: %s" % (text, pf() - start))

    shuffle(lst)
    sleep(3)
