"""Math - Matric"""
# Define function and variable
matric = {}

def create_matric(loop=1):
    '''Create matric'''
    for number in range(loop):
        print(f'\tMatric {number+1}')
        row = int(input('Row: '))
        column = int(input('Column: '))
        for x in range(row):
            line = input(f'Row - {x+1}: ')
            matric[number] = matric.get(number, [])+[(list(map(int, line.split())))]
        for i in matric[number]:
            print(end="[")
            for j in range(column):
                print('%5d'%(i[j]), end='|'*(j != column-1))
            print("]")
        matric[number] += [[row, column]]

def deteminate():
    '''Find determinate value'''
    for number in matric:
        det = 0
        row_col = matric[number][-1][0]
        for up in range(row_col-1*(row_col == 2)):
            total = 1
            for i in range(row_col):
                total *= matric[number][i][(up+i)%row_col]
            det += total
        for down in range(row_col-1*(row_col == 2)):
            total = 1
            for i in range(row_col)[::-1]:
                total *= matric[number][i][(down+range(row_col)[::-1][i])%row_col]
            det -= total
        print(f'Det {number+1}:', det)

def before_det():
    '''Check matric'''
    if matric[0][-1][0] == matric[0][-1][1]:
        deteminate()
    else:
        print("I can't find det value")
# Test call function
create_matric()
before_det()
