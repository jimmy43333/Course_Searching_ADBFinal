import csv #匯入csv模組
#打開名為20150421.csv的檔案，存於變數csvfile裡

def isnot_alphabet(uchar):         
    if (u'\u0041' <= uchar<=u'\u005a') or (u'\u0061' <= uchar<=u'\u007a'):
        return False
    else:
        return True

with open('teacher_data.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    data = []
    for row in readCSV:
        tmp =[row[0],row[1]]
        data.append(tmp)


with open('Teacher_Field.csv') as file:
    readField = csv.reader(file,delimiter=',')
    check = []
    for c in readField:
        check.append(c)

for ele in data:
    for f in check:
        if ele[1] in f[1]:
            ele.append(f[0])

f = open("teacher_Graph.csv","w")
w = csv.writer(f)
w.writerows(data)
f.close()