#!/usr/bin/env python
# coding: utf-8

# In[168]:


def find_zero(sdk):
    for row in range(9):
        for col in range(9):
            if sdk[row][col] == 0:
                return row, col
    return 101, 101


def correct(sdk, row,col,number):
    for i in range(9):
        if sdk[i][col]== number or sdk[row][i] == number:
            return False

    istart = row // 3
    jstart = col // 3

    for i in range(3*istart, 3*istart + 3):
        for j in range(3*jstart, 3*jstart + 3):
            if sdk[i][j]== number:
                return False
    return True

def solve(sdk):
    cell_y, cell_x = find_zero(sdk)
    if cell_x == 101:
        return True
    else:
        for number in range(1,10):
            if correct(sdk,cell_y,cell_x,number):
                sdk[cell_y][cell_x] = number
                if solve(sdk):
                    return True
                sdk[cell_y][cell_x] = 0
        return False
    
def print_sdk(sdk):
    for row in range(9):
        for col in range(9):
            print(sdk[row][col], end='')
        print()
        
path = input('Введите путь к файлу: ')

sdk = []
with open(path) as file:
    for line in file:
        line = line.strip()
        sdk.append([int(n) for n in line])
        
solve(sdk)  
print_sdk(sdk)

