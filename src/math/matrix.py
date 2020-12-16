"""Math - Matrix"""
# Define function
def error_int():
    '''Error input'''
    print("Error input (your input is not integer)!!")
    return False

def create_matrix(loop=1):
    '''Create matrix'''
    matrix = {}
    process = True
    for number in range(loop):
        print(f'\tMatrix {number+1}')
        try:
            row = int(input('Row: '))
            column = int(input('Column: '))
        except:
            process = error_int()
            break
        for x in range(row):
            line = input(f'Row - {x+1}: ')
            if len(line.split()) != column:
                process = False
                print('Wrong input!!!!')
                break
            matrix[number] = matrix.get(number, [])+[(list(map(int, line.split())))]
        if process:
            for i in matrix[number]:
                print(end="[")
                for j in range(column):
                    print('%5d'%(i[j]), end='|'*(j != column-1))
                print("]")
            print()
            matrix[number] += [[row, column]]
        else:
            print('Correct form'.center(30, '-'))
            print('| Row: 2'.ljust(30), end='|\n')
            print('| Column: 2'.ljust(30), end='|\n')
            print('| Row - 1: 2 6'.ljust(30), end='|\n')
            print('| Row - 2: 1 9'.ljust(30), end='|\n'+'-'*30)
    return process, matrix

def print_output(output, column):
    '''Print output matrix'''
    print('Answer', end='\n======\n')
    for i in output:
        print(end="[")
        for j in range(column):
            print('%5d'%(i[j]), end='|'*(j != column-1))
        print("]")

def addder(dimen, matrix, row=0):
    '''Addition'''
    output, column = matrix[0][:-1], dimen[1]
    for i in matrix[1][:-1]:
        col = 0
        for j in i:
            output[row][col] += j
            col += 1
        row += 1
    print_output(output, column)

def subtract(dimen, matrix, row=0):
    '''Subtraction'''
    output, column = matrix[0][:-1], dimen[1]
    for i in matrix[1][:-1]:
        col = 0
        for j in i:
            output[row][col] -= j
            col += 1
        row += 1
    print_output(output, column)

def multiple(matrix):
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

def determinant(out, matrix):
    '''Determinant'''
    det = 0
    row_col = matrix[0][-1][0]
    for up in range(row_col-1*(row_col == 2)):
        total = 1
        for i in range(row_col):
            total *= matrix[0][i][(up+i)%row_col]
        det += total
    for down in range(row_col-1*(row_col == 2)):
        total = 1
        for i in range(row_col)[::-1]:
            total *= matrix[0][i][(down+range(row_col)[::-1][i])%row_col]
        det -= total
    if out == 'A':
        print(f'\nDet {out}:', det)
    return det

def cramer(matrix):
    '''Cramer\'s rule'''
    char, constant, copy = [i for i in input('All variable: ').split()], [], {}
    time = matrix[0][-1]
    if len(char) != time[1]:
        print('Wrong input!!!!')
        print('Correct form'.center(30, '-'))
        print('| All variable: x y z (If you input 3 column)'.ljust(30), end='|\n'+'-'*30)
    else:
        print(f'\n\tConstant value')
        for i in range(time[0]):
            try:
                constant.append(int(input(f'Cons {i+1}: ')))
            except:
                error_int()
                break
        det_a = determinant('A', matrix)
        for i in range(time[1]):
            copy[0] = matrix[0].copy()
            for j in range(time[0]):
                copy[0][j][i] = constant[j]
            print(f'{char[i]} value:', (determinant(char[i], copy)/det_a))

def before_addsub(addsub, matrix):
    '''Check matrix'''
    if matrix[0][-1] == matrix[1][-1]:
        dimension = matrix[0][-1]
        if addsub == 'add':
            addder(dimension, matrix)
        else:
            subtract(dimension, matrix)
    else:
        print('Diffence shape')

def before_multi(matrix):
    '''Check matrix'''
    if matrix[0][-1][1] == matrix[1][-1][0]:
        multiple(matrix)
    else:
        print("I can't multiple this matrix")

def before_det(matrix):
    '''Check matrix'''
    if matrix[0][-1][0] == matrix[0][-1][1]:
        determinant('A', matrix)
    else:
        print("I can't find det value")

def before_cramer(matrix):
    '''Check matrix'''
    if matrix[0][-1][0] == matrix[0][-1][1]:
        cramer(matrix)
    else:
        print("It hard to use cramer's rule")

def add_sub(mode):
    '''Addition & Subtraction'''
    process, matrix = create_matrix(2)
    if process:
        before_addsub(mode, matrix)

def multi():
    '''Multiplication'''
    process, matrix = create_matrix(2)
    if process:
        before_multi(matrix)

def find_det():
    '''Determinant'''
    process, matrix = create_matrix()
    if process:
        before_det(matrix)

def find_cramer():
    '''Cramer\'s rule'''
    process, matrix = create_matrix()
    if process:
        before_cramer(matrix)
