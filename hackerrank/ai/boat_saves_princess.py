#!/usr/bin/python
def find_position(l, element):
    try:
        return l.index(element)
    except:
        return -1
    
def print_steps(n_times, step):
    for time in range(n_times):
        print(step)
    
def displayPathtoPrincess(n,grid):
    #print all the moves here
    princess_position = (-1,-1)
    boat_position = (-1,-1)
    for i, l in enumerate(grid):
        if princess_position[1] == -1:
            princess_position = (i, find_position(l, 'p'))
        if boat_position[1] == -1:
            boat_position = (i, find_position(l, 'm'))
        if princess_position[1] > -1 and boat_position[1] > -1:
            break
                             
    vertical_distance = princess_position[0] - boat_position[0]
    if vertical_distance < 0:
        #princess up boat
        print_steps(vertical_distance*-1, "UP")
    if vertical_distance > 0:
        print_steps(vertical_distance, "DOWN")
                             
    horizontal_distance = princess_position[1] - boat_position[1]
    if horizontal_distance < 0:
        print_steps(horizontal_distance*-1, "LEFT")
    if horizontal_distance > 0:
        print_steps(vertical_distance, "RIGHT")

                             
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)