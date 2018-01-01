import csv

def isnot_alphabet(uchar):         
    if (u'\u0041' <= uchar<=u'\u005a') or (u'\u0061' <= uchar<=u'\u007a'):
        return False
    else:
        return True

with open('CouseData_part2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') #以模組csv裡的函數reader來讀取csvfile變數，區隔符號為逗號(,)，讀取後存到readCSV變數裡
    dates = [] #宣告一個清單變數，名為dates
    for row in readCSV: #就readCSV裡的所有資料(以列為單位)
        while "" in row:
        	row.remove("")
        tmp = [row[0],row[2],row[3],row[4],row[5],row[8],row[9]]
        dates.append(tmp)

print(dates)  

f = open("course_part2.csv","w")
w = csv.writer(f)
w.writerows(dates)
f.close()
