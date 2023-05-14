import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
import numpy as np

#plt.figure(figsize = (12,30))
#plt.rcParams['font.family'] = 'Malgun Gothic'
x = list(range(12))
xval = [ '1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월' ]
area = [ '전국', '서울' ]

def main() -> int:

    f = open('jeju.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    index = np.arange(12)
    year = list()
    male = list()
    female = list()
    for row in data:
        if '시점' in row[0]:
            continue
        year.append(int(row[0]))
        male.append(int(row[2]))
        female.append(int(row[3]))
    f.close()

    if platform.system() == 'Darwin': #맥
        rc('font', family='AppleGothic')
    else: #그 외
        path = 'C:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font', family=font_name)
    
    fix, ax = plt.subplots(figsize=(12,6))
    bar_width = 0.25

    b1 = plt.bar(index + bar_width / 2, male, bar_width, alpha=0.4, color='blue', label='남성')
    b2 = plt.bar(index + bar_width * 3 / 2, female, bar_width, alpha=0.4, color='red', label='여성')
    
    plt.xticks(np.arange(bar_width, 12 + bar_width, 1), year)
    plt.title('제주특별자치도 연도별 남녀인구 수')
    plt.xlabel('연도', size = 13)
    plt.ylabel('인구 수(명)', size = 13)
    plt.legend()
    plt.show()
    return 0

# entry point of program
if __name__ == '__main__':
    main()
