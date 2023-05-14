import csv
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
#plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 7
count = [ '100번 시행', '1,000번 시행', '10,000번 시행', '100,000번 시행' ]
color = [ '#FF6363', '#FFD363','#6EE84F','#3797EF']

def main():

    dotone_K = list()
    one_K = list()
    ten_K = list()
    hundred_K = list()

    # 100번 시행 횟수 데이터 추출
    f = open('roll_100.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for row in data:
        dotone_K.append(int(row[1]))
    f.close()

    # 1,000번 시행 횟수 데이터 추출
    f = open('roll_1000.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for row in data:
        one_K.append(int(row[1]))
    f.close()

    # 10,000번 시행 횟수 데이터 추출
    f = open('roll_10000.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for row in data:
        ten_K.append(int(row[1]))
    f.close()

    # 100,000번 시행 횟수 데이터 추출
    f = open('roll_100000.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for row in data:
        hundred_K.append(int(row[1]))
    f.close()

    fig, axes = plt.subplots(2, 2)

    axes[0][0].hist(dotone_K, bins=6, histtype='bar', label=count[0],align='left', color=color[0])
    axes[0][0].set_title(count[0])
    axes[0][0].set_xlabel('주사위 숫자')
    axes[0][0].set_ylabel('시행 횟수')

    plt.subplot(222)
    axes[0][1].hist(one_K, bins=6, histtype='bar', label=count[1],align='left', color=color[1])
    axes[0][1].set_title(count[1])
    axes[0][1].set_xlabel('주사위 숫자')
    axes[0][1].set_ylabel('시행 횟수')

    plt.subplot(223)
    axes[1][0].hist(ten_K, bins=6, histtype='bar', label=count[2], align='left', color=color[2])
    axes[1][0].set_title(count[2])
    axes[1][0].set_xlabel('주사위 숫자')
    axes[1][0].set_ylabel('시행 횟수')

    plt.subplot(224)
    axes[1][1].hist(hundred_K, bins=6, histtype='bar', label=count[3], align='left', color=color[3])
    axes[1][1].set_title(count[3])
    axes[1][1].set_xlabel('주사위 숫자')
    axes[1][1].set_ylabel('시행 횟수')

    plt.suptitle("주사위 시뮬레이션",fontsize = 15)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.show()
    return 0

if __name__ =="__main__":
    main()