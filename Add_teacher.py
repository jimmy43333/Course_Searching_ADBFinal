import csv
from py2neo import Graph, Node, Relationship
#Add the Teacher node and relationship

p = input("GDB password:")
graph = Graph(password=p)

with open('./data/teacher_CF_Graph.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    teacher = []
    for row in readCSV:
        teacher.append(row)

ADB = graph.begin()
for item in teacher :
	#Build the node
	find = graph.find_one('Teacher', property_key='tname', property_value=item[1])
	tnode = Node("Teacher",teacher_id=item[0],tname=item[1])
	if find is None:
		ADB.merge(tnode,"Teacher","teacher_id")
	else:
		ADB.merge(tnode,"Teacher","tname")
	#Build the relationship with course_field
	cf_list = item[2:]
	for cf in cf_list:	
		cnode = graph.find_one('Course_Field', property_key='cf_id', property_value=cf)	
		if cnode is None:
			cnode = Node("Course_Field",cf_id=cf)
			ADB.merge(cnode,"Course_Field","cf_id")
		rel = Relationship(tnode,"expertise",cnode)
		ADB.merge(rel)
ADB.commit()