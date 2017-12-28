import csv
from py2neo import Graph, Node, Relationship
#Add the Area and Course Field node and relationship

p = input("GDB password:")
graph = Graph(password=p)

with open('./data/Area_Graph.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    Area = []
    for row in readCSV:
        Area.append(row)
with open('./data/courseField_A_Graph.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	Field = []
	for row in readCSV:
		Field.append(row)

ADB = graph.begin()
#Build the Area node
for item in Area:
	anode = Node("Area",A_id=item[0],name=item[1])
	ADB.merge(anode,"Area","A_id")
ADB.commit()

ADB = graph.begin()
#Build the course_field node and relationship
for item in Field:
	fnode = Node("Course_Field",cf_id=item[0],name=item[1])
	ADB.merge(fnode,"Course_Field","cf_id")
	anode = graph.find_one("Area",property_key="A_id", property_value=item[2])
	rel = Relationship(fnode,"belong",anode)
	
	ADB.merge(rel)
ADB.commit()