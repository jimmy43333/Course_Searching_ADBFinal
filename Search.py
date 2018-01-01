from py2neo import Graph, Node, Relationship, NodeSelector

def get_list_from_cursor(input):
	output = []
	for record in input:
		record_values = list(record.values())
		output.append(record_values)
	return output

p = input("GDB password:")
graph = Graph(password=p)

# Given a Teacher list
teacher = "Von-Wun Soo"
# find all the teacher in same course_field
statement = "MATCH (s)-[:expertise]->(m)<-[:expertise]-(g) WHERE s.tname=\""+ teacher +"\" RETURN m.name,g.tname"
#find all the teacher in the same Area
statement = "MATCH (s)-[:expertise]->()-[:belong]->(m)<-[:belong]-()<-[:expertise]-(g) WHERE s.tname=\""+ teacher +"\" RETURN m.name,g.tname"
# find all the course teached by this teacher
statement = "MATCH (g)-[:teach_by]->(s) WHERE s.tname= \"" + teacher + "\" RETURN g.course_id"

# Given a Area
area = "Computer and Communication Networks"
# find all the course_field
statement = "MATCH (s)-[:belong]->(g) WHERE e.name=\""+ area +"\" RETURN g.cf_id"

# Given a Course_field
coursefield = "Cloud Computing"
# find all the course
statement = "MATCH (s)-[:mention]->(e) WHERE e.name=\""+ cf +"\" RETURN e.name,s.course_id"

# Given a Course id 
select_course = "CS321201"
# find all the course in the same field
statement = "MATCH (s)-[:mention]->(m)<-[:mention]-(g) WHERE s.course_id=\""+ select_course +"\" RETURN m.name,g.course_id"
# find the advance course in the related field
statement = "MATCH (s)-[rs:mention]->(m)<-[rg:mention]-(g) WHERE s.course_id=\""+ select_course +"\" AND rg.weight >= rs.weight RETURN m.name,g.course_id,rg.weight"
# find the required
#statement = "MATCH (s:Course_Field)-[:required*1..100]->(g) RETURN g.course_id"


# Run the cypher
find = graph.run(statement)
output = get_list_from_cursor(find)