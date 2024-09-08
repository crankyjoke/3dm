import random
import os
from graphics.display import plot_3d_minefield



size_of_map = int(input("Choose size of map: "))
Number_of_Mine = 1

def get_coord(low, high, n):
    return random.sample(range(low, high), n)

x_coord = get_coord(0, size_of_map, Number_of_Mine)
y_coord = get_coord(0, size_of_map, Number_of_Mine)
z_coord = get_coord(0, size_of_map, Number_of_Mine)

displaygrid = [[['*' for _ in range(size_of_map)] for _ in range(size_of_map)] for _ in range(size_of_map)]
Mine_Map = [[[0 for _ in range(size_of_map)] for _ in range(size_of_map)] for _ in range(size_of_map)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_displaygrid():
    for i in range(size_of_map):
        print("----Layer" + " " + str(i) + "----")
        for j in range(size_of_map):
            print(' '.join(str(x) for x in displaygrid[i][j]))

clear_screen()


for i in range(Number_of_Mine):
    Mine_Map[z_coord[i]][y_coord[i]][x_coord[i]] = '!'

def count_number_mines(i, j, k):
    count_minee = 0
    operation_of_coord = [-1, 0, 1]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                if 0 <= i + operation_of_coord[a] < size_of_map and 0 <= j + operation_of_coord[b] < size_of_map and 0 <= k + operation_of_coord[c] < size_of_map:
                    if Mine_Map[i + operation_of_coord[a]][j + operation_of_coord[b]][k + operation_of_coord[c]] == "!":
                        count_minee += 1
    return count_minee

def fill_Mine_Map():
    for i in range(size_of_map):
        for j in range(size_of_map):
            for k in range(size_of_map):
                if Mine_Map[i][j][k] != "!":
                    Mine_Map[i][j][k] = count_number_mines(i, j, k)

fill_Mine_Map()

def print_Mine_Map():
    for i in range(size_of_map):
        print("----Layer" + " " + str(i) + "----")
        for j in range(size_of_map):
            print(' '.join(str(x) for x in Mine_Map[i][j]))

global triggered
triggered = False
global win
win = False

global list_of_mine
list_of_mine = dict()

for _ in range(Number_of_Mine):
    list_of_mine[z_coord[_], y_coord[_], x_coord[_]] = _

Mine_Marked = [False] * Number_of_Mine

def unreveal(q, visited, d):
    temp = []

    if len(q) == 0:
        return d
    for item in q:
        if [item[0], item[1], item[2]] in visited:
            pass
        else:
            visited.append([item[0], item[1], item[2]])
            if (item[0] + 1) < size_of_map:
                if Mine_Map[item[0] + 1][item[1]][item[2]] == 0:
                    temp.append([item[0] + 1, item[1], item[2]])
                    d[item[0] + 1][item[1]][item[2]] = 0
                else:
                    d[item[0] + 1][item[1]][item[2]] = Mine_Map[item[0] + 1][item[1]][item[2]]

            if (item[1] + 1) < size_of_map:
                if Mine_Map[item[0]][item[1] + 1][item[2]] == 0:
                    temp.append([item[0], item[1] + 1, item[2]])
                    d[item[0]][item[1] + 1][item[2]] = 0
                else:
                    d[item[0]][item[1] + 1][item[2]] = Mine_Map[item[0]][item[1] + 1][item[2]]

            if (item[2] + 1) < size_of_map:
                if Mine_Map[item[0]][item[1]][item[2] + 1] == 0:
                    temp.append([item[0], item[1], item[2] + 1])
                    d[item[0]][item[1]][item[2] + 1] = 0
                else:
                    d[item[0]][item[1]][item[2] + 1] = Mine_Map[item[0]][item[1]][item[2] + 1]

            if (item[0] - 1) >= 0:
                if Mine_Map[item[0] - 1][item[1]][item[2]] == 0:
                    temp.append([item[0] - 1, item[1], item[2]])
                    d[item[0] - 1][item[1]][item[2]] = 0
                else:
                    d[item[0] - 1][item[1]][item[2]] = Mine_Map[item[0] - 1][item[1]][item[2]]

            if (item[1] - 1) >= 0:
                if Mine_Map[item[0]][item[1] - 1][item[2]] == 0:
                    temp.append([item[0], item[1] - 1, item[2]])
                    d[item[0]][item[1] - 1][item[2]] = 0
                else:
                    d[item[0]][item[1] - 1][item[2]] = Mine_Map[item[0]][item[1] - 1][item[2]]

            if (item[2] - 1) >= 0:
                if Mine_Map[item[0]][item[1]][item[2] - 1] == 0:
                    temp.append([item[0], item[1], item[2] - 1])
                    d[item[0]][item[1]][item[2] - 1] = 0
                else:
                    d[item[0]][item[1]][item[2] - 1] = Mine_Map[item[0]][item[1]][item[2] - 1]

    unreveal(temp, visited, d)

def click(z, y, x, action_type):
    if action_type == 1:  # click
        if Mine_Map[z][y][x] == "!":
            return True
        else:
            displaygrid[z][y][x] = Mine_Map[z][y][x]
            if Mine_Map[z][y][x] == 0:
                q = [[z, y, x]]
                unreveal(q, [], displaygrid)
    elif action_type == 2:  # mark
        displaygrid[z][y][x] = "?"
    elif action_type == 3:  # flag
        displaygrid[z][y][x] = "^"
        if Mine_Map[z][y][x] == "!":
            Mine_Marked[list_of_mine[(z, y, x)]] = True
    elif action_type == 4:
        if displaygrid[z][y][x] == "^" or displaygrid[z][y][x] == "?":
            displaygrid[z][y][x] = "*"
            if Mine_Map[z][y][x] == "!":
                Mine_Marked[list_of_mine[(z, y, x)]] = False
    else:
        pass

def check_win():
    for mines in Mine_Marked:
        if not mines:
            return False
    return True

def print_message_box(message):
    print("="*len(message))
    print(message)
    print("="*len(message))

while not triggered and not win:
    clear_screen()
    print_displaygrid()
    print_message_box("Choose movement type (1: reveal, 2: mark, 3: flag, 4: unmark):")
    mt = int(input())
    print_message_box("Choose location (x y z):")
    plot_3d_minefield(displaygrid, size_of_map)
    x, y, z = map(int, input().split(" "))

    if click(z, y, x, mt):
        triggered = True
    else:
        win = check_win()

clear_screen()
if triggered:
    print_message_box("BOMB ACTIVATED")
else:
    print_message_box("BOMB DEFUSED")
print_displaygrid()



