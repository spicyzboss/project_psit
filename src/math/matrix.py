"""Math - Matrix"""
# Define function and variable
matrix = {}

def create_matrix(loop=1):
    '''Create matrix'''
    global process
    for number in range(loop):
        print(f'\tMatrix {number+1}')
        try:
            process = True
            row = int(input('Row: '))
            column = int(input('Column: '))
        except:
            print('You can input only integer\n')
            process = False
            break
        for x in range(row):
            line = input(f'Row - {x+1}: ')
            if len(line.split()) != column:
                process = False
            matrix[number] = matrix.get(number, [])+[(list(map(int, line.split())))]
        if process:
            for i in matrix[number]:
                print(end="[")
                for j in range(column):
                    print('%5d'%(i[j]), end='|'*(j != column-1))
                print("]")
        print()
        matrix[number] += [[row, column]]

def addder(dimen, row=0):
    '''Addition'''
    output, column = matrix[0][:-1], dimen[1]
    for i in matrix[1][:-1]:
        col = 0
        for j in i:
            output[row][col] += j
            col += 1
        row += 1
    print_output(output, column)

def subtract(dimen, row=0):
    '''Subtraction'''
    output, column = matrix[0][:-1], dimen[1]
    for i in matrix[1][:-1]:
        col = 0
        for j in i:
            output[row][col] -= j
            col += 1
        row += 1
    print_output(output, column)

def multiple():
    '''Multiplication'''
    output = []
    mxt1, mxt2 = matrix[0], matrix[1]
    for x in range(mxt1[-1][0]):
        run = []
        for _ in range(mxt1[-1][1]):
            for i in range(mxt2[-1][1]):
                run += [sum([mxt1[x][y]*mxt2[y][i] for y in range(mxt2[-1][0])])]
        output.append(run)
    print_output(output, mxt2[-1][1])

def determinant():
    '''Determinant'''
    for number in matrix:
        det = 0
        row_col = matrix[number][-1][0]
        for up in range(row_col-1*(row_col == 2)):
            total = 1
            for i in range(row_col):
                total *= matrix[number][i][(up+i)%row_col]
            det += total
        for down in range(row_col-1*(row_col == 2)):
            total = 1
            for i in range(row_col)[::-1]:
                total *= matrix[number][i][(down+range(row_col)[::-1][i])%row_col]
            det -= total
        print(f'Det {number+1}:', det)

def cramer():
    '''Cramer\'s rule'''

def print_output(output, column):
    '''Print output matrix'''
    print('Answer', end='\n======\n')
    for i in output:
        print(end="[")
        for j in range(column):
            print('%5d'%(i[j]), end='|'*(j != column-1))
        print("]")

def before_addsub(addsub):
    '''Check matrix'''
    if matrix[0][-1] == matrix[1][-1]:
        dimension = matrix[0][-1]
        if addsub == 'add':
            addder(dimension)
        else:
            subtract(dimension)
    else:
        print('Diffence shape')

def before_multi():
    '''Check matrix'''
    if matrix[0][-1] == matrix[1][-1][::-1]:
        multiple()
    else:
        print("I can't multiple this matrix")

def before_det():
    '''Check matrix'''
    if matrix[0][-1][0] == matrix[0][-1][1]:
        determinant()
    else:
        print("I can't find det value")

def add_sub(mode):
    '''Addition & Subtraction'''
    create_matrix(2)
    if process:
        before_addsub(mode)

def multi():
    '''Multiplication'''
    create_matrix(2)
    if process:
        before_multi()

def find_det():
    '''Determinant'''
    create_matrix()
    if process:
        before_det()

def find_cramer():
    '''Cramer\'s rule'''
    if process:
        create_matrix()
