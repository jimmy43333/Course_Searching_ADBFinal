import csv
from py2neo import Graph, Node, Relationship
#Add the Course node and relationship

p = input("GDB password:")
graph = Graph(password=p)

with open('./data/course_CF_Graph.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    course = []
    for row in readCSV:
        course.append(row)

with open('./data/course_T_Graph.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    c_t = []
    for row in readCSV:
        c_t.append(row)

ADB = graph.begin()
for item in course :
	#Build the node
	cnode = Node("Course",course_id=item[0],title=item[1])
	ADB.merge(cnode,"Course","course_id")
	#Build the relationship with course_field
	field_list = item[2:]
	for ele in field_list:
		cut = ele.split(",")
		fnode = graph.find_one('Course_Field', property_key='cf_id', property_value=cut[0])
		if fnode is None:
			fnode = Node('Course_Field',cf_id=cut[0])
		rel = Relationship(cnode,"mention",fnode,weight=int(cut[1]))
		ADB.merge(fnode,"Course_Field","cf_id")
		ADB.merge(rel)
ADB.commit()

#Build the relationship with teacher
ADB = graph.begin()
for item in c_t: 
	mul_teacher = item[2].split(",")
	cnode = graph.find_one('Course', property_key='course_id', property_value=item[0])
	if cnode is None:
		cnode = Node("Course",course_id=item[0],title=item[1])
	for t in mul_teacher:
		tnode = graph.find_one('Teacher', property_key='teacher_id', property_value=t)
		if tnode is None:
			if ' ' in t:
				tnode = Node("Teacher",tname=t,teacher_id="0")
				ADB.merge(tnode,"Teacher","tname")
			else:
				tnode = Node("Teacher",teacher_id=t)
				ADB.merge(tnode,"Teacher","teacher_id")
		rel = Relationship(cnode,"teach_by",tnode)
		ADB.merge(rel)
ADB.commit()