import numpy as np
import math

class Orchard:
    rows = 1000
    columns = 1000

    matrix = None

    def __init__(self):

        self.matrix = np.zeros((self.rows, self.columns), dtype=int)

        # self.matrix[0][1] = 1
        # self.matrix[1][0] = 1

        # print(self.matrix)

    def is_prepared(self, row, column):
        return self.matrix[row][column] == 1

    def get_surrounding(self, row, column):
        return self.matrix[row-1:row+2,column-1:column+2]

    def number_of_prepped(self, array):
        unique, counts = np.unique(array, return_counts=True)

        self.amounts = dict(zip(list(unique), list(counts)))

        return self.amounts

output_file = ''

def reset_file():
    global output_file
    # output_file = open('output', 'w')
    # output_file.write("")
    # output_file.close()
    # output_file = open('output', 'a')


def Print(output):
    global output_file
    # output_file.write(str(output))

def do_test_case():
    global output_file

    Print('\n============Test case============\n')


    a = int(input())
    Print('A: ' + str(a) + '\n')

    orchard = Orchard()

    part = orchard.get_surrounding(1, 1)
    orchard.number_of_prepped(part)

    rows = math.ceil(math.sqrt(a))
    columns = math.ceil(a / rows)

    Print('Rows x Columns: \n')
    Print(str((rows, columns)) + '\n')

    global attempts
    attempts = 0

    Print('We want: rows {} to {} and columns {} to {} \n'.format(2, 2+rows, 2, 2+columns))

    def give_input_get_response(string):
        print(string)
        Print('Input given: {} \n'.format(string))

        response = input()

        Print('Response: {} \n'.format(response))

        return response

    global done
    done = False

    def do_block(center_row, center_column):
        global done
        if done:
            return

        for i in range(80):
            test = give_input_get_response(str(center_row) + ' ' + str(center_column))

            global attempts
            attempts += 1

            test = test.split(" ")
            test = list(map(int, test))

            if np.count_nonzero(orchard.get_surrounding(center_row, center_column)) == 9:
                break

            if test[0] == 0 and test[1] == 0:
                Print('Done\n')
                Print('Attempts: {}\n'.format(attempts))
                orchard.matrix[test[0]][test[1]] = 1
                done = True
                return

            orchard.matrix[test[0]][test[1]] = 1

    # for i in range(1,2):
        # for j in range(1,2):
            # print(i*3, j*3)
            # if not done:
                # do_block(3*i, 3*j)

    do_block(3, 3)
    do_block(3, 6)
    do_block(3, 9)

    do_block(6, 3)
    do_block(6, 6)
    do_block(6, 9)

    do_block(9, 3)
    do_block(9, 6)
    do_block(9, 9)

    Print(str(orchard.matrix[:10,:10]) + '\n')

reset_file()

t = int(input())
Print('T: ' + str(t) + '\n')

for i in range(t):
    do_test_case()
