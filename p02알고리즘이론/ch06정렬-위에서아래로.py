def 위에서아래로():
    n = int(input())
    array = []

    for i in range(n):
        array.append(int(input()))

    array.sorted(array, reverse=True)

    for i in array:
        print(i, end=' ')
if __name__ == '__main__':
    위에서아래로()