import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

x = list(range(30))

def main() -> int:
    f = open('2023_03_station.csv', 'r', encoding='utf8')
    data = csv.reader(f, delimiter=',')
    next(data)
    next(data)
    getOn = dict()
    getOff = dict()
    total = dict()
    for row in data:
        key = (row[1], row[3])
        if not key in getOn:
            getOn[key] = 0
            getOff[key] = 0
            total[key] = 0

            getOn[key] += int(row[4]) + int(row[6])
            getOff[key] += int(row[5]) + int(row[7])
            total[key] += int(row[4]) + int(row[5]) + int(row[6]) + int(row[7])
    f.close()
    getOn30 = sorted(getOn.items(), key = lambda item: item[1], reverse = True)[:30]
    getOn30Stations = list()
    getOn30Persons = list()
    for t in getOn30:
        getOn30Stations.append('{} {}'.format(t[0][0], t[0][1]))
        getOn30Persons.append(t[1])

    if platform.system() == 'Darwin': #맥
        rc('font', family='AppleGothic')
    else: #그외
        path = 'C:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font', family=font_name)

    plt.figure(figsize=(10,5))
    plt.xticks(rotation=90)
    plt.bar(getOn30Stations, getOn30Persons, color='limegreen', width = 0.7)
    plt.title('2023년 3월 출근 시간 최대 승차역 30개')
    plt.xlabel('지하철 역 이름')
    plt.ylabel('이용자 수')
    plt.tight_layout()
    plt.show()

# entry point of program
if __name__ == '__main__':
	main()
