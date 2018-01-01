import csv #匯入csv模組
#打開名為20150421.csv的檔案，存於變數csvfile裡

def isnot_alphabet(uchar):         
    if (u'\u0041' <= uchar<=u'\u005a') or (u'\u0061' <= uchar<=u'\u007a'):
        return False
    else:
        return True

with open('course_part2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',') #以模組csv裡的函數reader來讀取csvfile變數，區隔符號為逗號(,)，讀取後存到readCSV變數裡
    dates = [] #宣告一個清單變數，名為dates
    for row in readCSV: #就readCSV裡的所有資料(以列為單位)
        tmp = [row[0],row[1],row[5].title()]
        dates.append(tmp)                

with open('../data/teacher_CF_Graph.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    output=[]
    out = []
    for row in readCSV:
        output.append([row[0],row[1]])

for d in dates:
    name = d[2].split(" ")
    if len(name)==3:
        tmp = name[0]
        name[0] = name[1]
        name[1] = name[2]
        name[2] = tmp
        name = ' '.join(name)

    for a in output:
        if "," in name:
            t = name.split(',')
            for k in t:
                if k ==a[1]:
                    k = a[0]
            d[2] = t
        if name == a[1]:
            d[2] = a[0]

print(dates)

f = open("Course_T_Graph02.csv","w")
w = csv.writer(f)
w.writerows(dates)
f.close()
