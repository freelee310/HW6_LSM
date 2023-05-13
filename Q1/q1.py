import csv
import matplotlib.pyplot as plt

plt.figure(figsize = (12,10))
plt.rcParams['font.family'] = 'AppleGothic'
#plt.rcParams['font.family'] = 'Malgun Gothic'
x = list(range(12))
xval = [ '1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월' ]
plt.title('평균기온')
plt.xlabel('월', size=12)
plt.ylabel('기온( ℃ )', size=12)
plt.xticks(x, xval)
area = list()

def main() -> int:

    # 서울 평균 기온 추출
    f = open('2022_Seoul.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    seoul = list()
    for row in data:
        if len(row) < 2 or not '108' in row[1]:
            continue
        seoul.append(float(row[2]))
    f.close()
    area.append('서울')

    # 대전 평균 기온 추출
    f = open('2022_Daejeon.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    daejeon = list()
    for row in data:
        if len(row) < 2 or not '133' in row[1]:
            continue
        daejeon.append(float(row[2]))
    f.close()
    area.append('대전')

    # 부산 평균 기온 추출
    f = open('2022_Busan.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    busan = list()
    for row in data:
        if len(row) < 2 or not '159' in row[1]:
            continue
        busan.append(float(row[2]))
    f.close()
    area.append('부산')

    # 제주 평균 기온 추출
    f = open('2022_Jeju.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    jeju = list()
    for row in data:
        if len(row) < 2 or not '제주' in row[1]:
            continue
        jeju.append(float(row[2]))
    f.close()
    area.append('제주')

    # 전국 평균 기온 추출
    f = open('2022_Korea.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')

    korea = list()
    for row in data:
        if len(row) < 2 or not '전국' in row[1]:
            continue
        korea.append(float(row[2]))
    f.close()
    area.append('전국')

#    fig, ax = plt.subplots(figsize=(12,12))
#    plt.yscale('log')

    plt.plot(x, seoul, marker='.', color='royalblue', label='서울')
    for index in x:
        plt.text(x[index], seoul[index], seoul[index], size=8, color='royalblue')

    plt.plot(x, daejeon, marker='.', color='limegreen', label='대전')
    for index in x:
        plt.text(x[index], daejeon[index], daejeon[index], size=8, color='limegreen')

    plt.plot(x, busan, marker='.', color='darkviolet', label='부산')
    for index in x:
        plt.text(x[index], busan[index], busan[index], size=8, color='darkviolet')

    plt.plot(x, jeju, marker='.', color='orange', label='제주')
    for index in x:
        plt.text(x[index], jeju[index], jeju[index], size=8, color='orange')

    plt.plot(x, korea, linestyle='dashed', marker='o', color='tomato', label='전국')
    for index in x:
        plt.text(x[index], korea[index], korea[index], size=8, color='tomato')

    plt.legend(area)
    plt.show()


    return 0

# entry point of program
if __name__ == '__main__':
	main()