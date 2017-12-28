from py2neo import Graph, Node, Relationship, NodeSelector

def get_list_from_cursor(input):
	output = []
	for record in input:
		record_values = list(record.values())
		output.append(record_values)
	print(output)

p = input("GDB password:")
graph = Graph(password=p)


teacher = "Von-Wun Soo"
result = graph.run("MATCH (s)-[:expertise]->(m)<-[:expertise]-(g) WHERE s.tname=\""+ teacher +"\" RETURN s.tname,m.name,g.teacher_id")
output = get_list_from_cursor(result)
