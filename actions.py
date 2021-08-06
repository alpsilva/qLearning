import random

def move(state, direction):

    # grid mostrando a posição de cada estado
    # 5 -> Obstáculo
    # 10, 11, 12 -> Estados terminais
    grid = [
        [2, 5, 8, 11],
        [1, 4, 7, 10],
        [0, 3, 6, 9]
    ]

    agentX = 0
    agentY = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == state:
                agentX = i
                agentY = j

    # Baseado no movimento que o agente tentou fazer, define randomicamente qual será executado:
    # 0.8 chance de ser o que o agente queria
    # 0.1 chance de ir para a esquerda ao invés do que ele queria
    # 0.1 chance de ir para a direita ao invés do que ele queria

    rd = random.randint(1,10)

    trueMove = ''

    if direction == 0:
        if rd < 2:
            trueMove = 'l'
        elif rd > 9:
            trueMove = 'r'
        else:
            trueMove = 'u'
    elif direction == 1:
        if rd < 2:
            trueMove = 'r'
        elif rd > 9:
            trueMove = 'l'
        else:
            trueMove = 'd'
    elif direction == 2:
        if rd < 2:
            trueMove = 'd'
        elif rd > 9:
            trueMove = 'u'
        else:
            trueMove = 'l'
    elif direction == 3:
        if rd < 2:
            trueMove = 'u'
        elif rd > 9:
            trueMove = 'd'
        else:
            trueMove = 'r'

    xLim = len(grid)
    yLim = len(grid[0])

    newX = agentX
    newY = agentY

    if trueMove == 'u':
        # (x-1, y)
        newX -= 1
    elif trueMove == 'd':
        # (x+1, y)
        newX += 1
    elif trueMove == 'l':
        # (x, y-1)
        newY -= 1
    elif trueMove == 'r':
        # (x, y+1)
        newY += 1

    if newX >= xLim:
        newX -= 1
    if newX < 0:
        newX = 0

    if newY >= yLim:
        newY -= 1
    if newY < 0:
        newY = 0

    # checa se bateu no obstáculo
    if (newX == 1 and newY == 1):
        newX = agentX
        newY = agentY

    return grid[newX][newY]

def choose_random_action():
    rd = rd = random.randint(0,3)
    return rd