#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k, j in enumerate(i):
            if k == len(i) - 1:
                print('{}'.format(j))
            else:
                print('{}'.format(j), end=' ')


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
