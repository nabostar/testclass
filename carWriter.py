import csv

with open('차량관리.csv','w')as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1,'08러1234','2020-10-20,14:00'])
    csv_maker.writerow([2,'25다1234','2020-10-20,14:00'])
    csv_maker.writerow([3,'28하1234','2020-10-20,14:00'])
print('차량관리.csv파일이 생성되었습니다.')