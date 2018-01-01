# Course_Searching_ADBFinal


## Area
property: { A_id, name } 
relation: 

## Course_Field
property: { cf_id, name } 
relation: (CF)-[belong:]->(A)

## Course 
property: { course_id, title } 
relation: (C)-[mention:weight]->(CF) 
          (C)-[teach_by]->(T) 

## Teacher 
property: { teacher_id, tname } 
relation: (T)-[:expertise]->(CF) 

## Reference
https://www.slideshare.net/leezhenyu/coscup-2016-workshop-neo4j
