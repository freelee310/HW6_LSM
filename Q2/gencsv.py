import csv
import random

def gencsv(try_num):
    results = []  # 주사위 결과를 저장할 리스트

    for i in range(try_num):
        dice_roll = random.randint(1, 6)
        results.append(dice_roll)

    f = open('roll_{}.csv'.format(try_num), 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    row = 1
    for result in results:
        wr.writerow([row, result])
        row += 1
    f.close()

def main() -> int:

    random.seed()

    try_count = [ 100, 1000, 10000, 100000 ]
    for c in try_count:
        gencsv(c)
    return 0

# entry point of program
if __name__ == '__main__':
    main()