import csv

class Student:

    def __init__(self, studentId, studentName, studentMarks):
        self.studentId = studentId
        self.studenName = studentName
        self.studentMarks = studentMarks

    def __repr__(self):
        return f"Student({self.studentId},{self.studenName},{self.studentMarks})"
    
    
    def writeToCsv(self):
        return [self.studentId, self.studenName, self.studentMarks]
    
    @classmethod
    def readFromCsv(cls, row):
        studentId, studentName, studentMarks = row
        return cls(int(studentId), studentName, int(studentMarks))
    
students = [
    Student(1, "Abhishek" , 10),
    Student(2, "ABC" , 20),
    Student(3, "XYZ", 30),
    Student(4, "PQR", 40)
]

def writeStudentsToCsv(students, filename = 'students.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['studentId', 'studentName', 'studentMarks'])

        for student in students:
            writer.writerow(student.writeToCsv())


def readStudentsFromCsv(filename = 'students.csv'):
    students.clear()
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            students.append(Student.readFromCsv(row))

writeStudentsToCsv(students)

# readStudentsFromCsv()
# for stu in students:
#     print(stu)


#writeStudentsToCsv(students)




    

        
    

        