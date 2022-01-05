# Pair Programming
"""
The test results of six different students are presented 
below. Each student has gotten a number score ranging 
between 0 and 100 from 5 of their most recent tests.

Student1: 70.5, 88.0, 91.0, 85.5, 66.5
Student2: 90.5, 92.5, 90.0, 95.0, 87.5
Student3: 75.5, 75.0, 77.0, 75.5, 81.5
Student4: 55.5, 68.0, 71.5, 85.0, 66.0
Student5: 70.5, 88.0, 91.0, 85.5, 66.5
Student6: 80.5, 87.0, 57.0, 75.5, 64.0

Arrange the data in a suitable format. Write code that 
for each student prints "Student X 
has an average score of Y" where X is the student number/name 
and Y is the average or mean of the students' test results. 
After this, print a single sentence that says "Student X has 
gotten a score of less than 60% => Z" where Z is the score 
that is below 60. Only do this for students that have gotten a 
test result below 60.
"""

studentDict = {
	"Student 1": [70.5, 88.0, 91.0, 85.5, 66.5],
	"Student 2": [90.5, 92.5, 90.0, 95.0, 87.5],
	"Student 3": [75.5, 75.0, 77.0, 75.5, 81.5],
	"Student 4": [55.5, 68.0, 71.5, 85.0, 66.0],
	"Student 5": [70.5, 88.0, 91.0, 85.5, 66.5],
	"Student 6": [80.5, 87.0, 57.0, 75.5, 64.0]
}

msg = ''
for student in studentDict:
	resultsList = studentDict[student]

	total = sum(resultsList)
	average = total/len(resultsList)

	print(f'{student} has an average score of {average}')

	for result in resultsList:
		if result < 60:
			msg += f"{student} has gotten a score of less than 60% => {result}\n"

print(msg)