"""Math - Matrix"""
# Define function
def main():
    '''Define and clear variable'''
    global matrix
    global process
    matrix = {}
    process = True

def error_int():
    '''Error input'''
    global process
    print("Error input (your input is not integer)!!")
    process = False

def create_matrix(loop=1):
    '''Create matrix'''
    global process
    for number in range(loop):
        print(f'\tMatrix {number+1}')
        try:
            row = int(input('Row: '))
            column = int(input('Column: '))
        except:
            error_int()
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

def determinant(out):
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
        print(f'Det {out}:', det)
    return det

def cramer():
    '''Cramer\'s rule'''
    global matrix
    char, constant = [i for i in input('All variable: ').split()], []
    time = matrix[0][-1]
    if len(char) != time[1]:
        print('Wrong input!!!!')
        print('Correct form'.center(30, '-'))
        print('| All variable: x y z (If you input 3 column)'.ljust(30), end='|\n'+'-'*30)
    else:
        print(f'\tConstant value')
        for i in range(time[0]):
            try:
                constant.append(int(input(f'Cons {i+1}: ')))
            except:
                error_int()
                break
        det_a = determinant('A')
        for i in range(time[1]):
            copy = matrix
            for j in range(time[0]):
                matrix[0][j][i] = constant[j]
            print(f'{char[i]} value:', determinant(char[i])/det_a)
            matrix = copy

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
        determinant('A')
    else:
        print("I can't find det value")

def before_cramer():
    '''Check matrix'''
    if matrix[0][-1][0] == matrix[0][-1][1]:
        cramer()
    else:
        print("It hard to use cramer's rule")

def add_sub(mode):
    '''Addition & Subtraction'''
    main()
    create_matrix(2)
    if process:
        before_addsub(mode)

def multi():
    '''Multiplication'''
    main()
    create_matrix(2)
    if process:
        before_multi()

def find_det():
    '''Determinant'''
    main()
    create_matrix()
    if process:
        before_det()

def find_cramer():
    '''Cramer\'s rule'''
    main()
    create_matrix()
    if process:
        before_cramer()
