#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print('{}'.format(j), end=' ')
        print()


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
