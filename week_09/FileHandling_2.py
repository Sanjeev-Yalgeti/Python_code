class Employee:
    def __init__(self,empid,ename,dept,salary):
        self.empid=empid
        self.ename=ename
        self.dept=dept
        self.salary=salary
    def to_string(self):
        return f"{self.empid} {self.ename} {self.dept} {self.salary}"
class EmployeeManager:
    def __init__(self,filename):
        self.filename=filename
    def addRecords(self):
        empid=input("Enter Employee id :")
        ename=input("Enter Employee name :")
        dept=input("Enter Department Name :")
        salary=int(input("Enter Salary:"))
        s1=Employee(empid,ename,dept,salary)
        with open(self.filename,"a") as f:
            f.write(f"{s1.to_string()}"+"\n")
        print("Record added successfully")
    def viewRecords(self):
        try:
            with open(self.filename,"r") as f:
                records=f.readlines()
                for i in records:
                    print(i)
        except FileNotFoundError:
            print("File not Found")

    def totalSalaryExpense(self):
        try:
            expense=0
            with open(self.filename,"r") as f:
                records=f.readlines()
                for line in records:
                    expense+=int(line.strip().split()[3])
                print(f"Total Salary :{expense}")
        except FileNotFoundError:
            print("Total Salary :0")
if __name__=="__main__":
    loop=1
    while loop:
        print(10*"*"+"Menu"+10*"*"+"\n1.Add Employee Records \n2.View Employee Records \n3.Calculate total expense \n4.Exit")
        ch=int(input("Enter A choice ::"))
        manager=EmployeeManager("employees.txt")
        if ch<=4:
            match ch:
                case 1:
                    manager.addRecords()
                case 2:
                    manager.viewRecords()
                case 3:
                    manager.totalSalaryExpense()
                case 4:
                    loop=0
        else:
            print("Enter Valid Choice ::")
        print(25*"*")     

        
            

