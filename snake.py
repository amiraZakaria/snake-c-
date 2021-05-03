import random

N, M = 6, 15
counter = 0
a, b = -1, -1
grid = [['+' for x in range(M)] for y in range(N)]


# This function prints the grid of Gomoku as the game progresses
def print_grid():
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
    print('--' + '---' * M + '--')

# This function checks if the game has a tie state or not for the given mark
def check_lose(i,a,b):
    if i == 3:
        if grid[a][b + 1] == '-':
            return True
    elif i == 1:
        if grid[a - 1][b] == '-':
            return True
    elif i == 2:
        if grid[a + 1][b] == '-':
            return True
    elif i == 4:
        if grid[a][b - 1] == '-':
            return True
    return False


def check_eat(i,a,b):
    global counter
    if i == 3:
        if grid[a][b + 1] == '+':
            grid[a][b] = '_'
            grid[a][b+1]='0'
            b+=1
            counter+=1
            return True
    elif i == 1:
        if grid[a - 1][b] == '+':
            grid[a][b] = '_'
            grid[a-1][b] = '0'
            a -= 1
            counter += 1
            return True

    elif i == 2:
        if grid[a + 1][b] == '+':
            grid[a][b] = '_'
            grid[a+1][b] = '0'
            a += 1
            counter += 1
            return True

    elif i == 4:
        if grid[a][b - 1] == '+':
            grid[a][b] = '_'
            grid[a][b - 1] = '0'
            b -= 1
            counter += 1
            return True

    return False


def move(i):
    global x
    global y

    global a
    global b
    global counter
    grid[a][b] = '.'

    if counter>=1:

      if i == 3:  # right

            grid[x][y] = ' '
            grid[a][b + 1] = '0'
            grid[a][b] = '_'

            b += 1

      elif i == 1:  # up
          grid[x][y] = ' '
          grid[a-1][b] = '0'
          grid[a][b] = '_'

          a -= 1

      elif i == 2:  # down
          grid[x][y] = ' '
          grid[a+1][b] = '0'
          grid[a][b] = '_'
          a += 1

      elif i == 4:  # left
          grid[x][y] = ' '
          grid[a][b - 1] = '0'
          grid[a][b] = '_'

          b -= 1


# This function generates pac man
def generate_snake():
    global a
    global b
    a = random.randint(0, N - 1)
    b = random.randint(0, M - 1)
    grid[a][b] = '0'


# This function generates ghosts
def generate_apple():
        a = random.randint(0, N - 1)
        b = random.randint(0, M - 1)
        while grid[a][b] == '0' or grid[a][b] == '0':
            a = random.randint(0, N - 1)
            b = random.randint(0, M - 1)
        grid[a][b] = '+'

# This function checks if given position is valid or not
def check_valid_direction(i):
    if i == 1 or i == 2 or i == 3 or i == 4:
        return True
    else:
        return False


# This function clears the game structures
def grid_clear():
    global grid
    grid = [[' ' for x in range(M)] for y in range(N)]
    global counter
    counter = 0


# This function reads a valid position input
def read_input():
    i = int(input('Enter the direction: '))
    while not check_valid_direction(i):
        i = int(input('Enter a valid direction: '))
    return i


# MAIN FUNCTION
def play_game():
    print("snake Game!")
    print("Welcome...")
    print("============================")
    while True:
        # Prints the grid
        print_grid()
        i = read_input()
        # Check if the grid has a tie state
        if check_lose(i,a,b):
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            print("GAME OVER!")
            break
        if check_eat(i,a,b):
            print_grid()
            generate_apple()
        else:
            move(i)
            print("your score :", counter)

while True:
    grid_clear()
    generate_snake()
    generate_apple()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
