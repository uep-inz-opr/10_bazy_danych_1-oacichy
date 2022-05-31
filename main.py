import csv

if __name__ == '__main__':
    plik = input()
    data = csv.reader(open(plik))
    next(data)
    sum = 0
    for row in data:
        value = int(row[3])
        sum += value

    print(sum)

