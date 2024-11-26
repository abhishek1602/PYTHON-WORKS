class Employee:

    def __init__(self, empId, empName, empNumber, empLocation):
        self.empId = empId
        self.empName = empName
        self.empNumber = empNumber
        self.empLocation = empLocation

    def __repr__(self):
        return f"Employee({self.empId}, {self.empName}, {self.empNumber}, {self.empLocation})"

    def to_dict(self):
        return {
            "empId": self.empId,
            "empName": self.empName,
            "empNumber": self.empNumber,
            "empLocation": self.empLocation
        }
