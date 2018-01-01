from py2neo import Graph, Node, Relationship, NodeSelector

def get_list_from_cursor(input):
	output = []
	for record in input:
		record_values = list(record.values())
		output.append(record_values)
	print(output)

p = input("GDB password:")
graph = Graph(password=p)

select_course = "CS321201"
statement = "MATCH (s)-[rs:mention]->(m)<-[rg:mention]-(g) WHERE s.course_id=\""+ select_course +"\" AND rg.weight > rs.weight RETURN m.name,g.course_id,rg.weight"

result = graph.run(statement)
output = get_list_from_cursor(result)
