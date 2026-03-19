class Student:
    def __init__(self,sid,sname,cname,feeStatus):
        self.sid=sid
        self.sname=sname
        self.cname=cname
        self.feeStatus=feeStatus
    def to_string(self):
        return f"{self.sid} {self.sname} {self.cname} {self.feeStatus}"
class StudentManager:
    def __init__(self,filename):
        self.filename=filename
    def addRecords(self):
        sid=int(input("Enter Student id :"))
        sname=input("Enter Student name :")
        cname=input("Enter Course Name :")
        feeStatus=int(input("Enter fee amount:"))
        s1=Student(sid,sname,cname,feeStatus)
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

    def searchId(self):
        id=int(input("Enter Id to be searched :"))
        try:
            found=False
            with open(self.filename,"r") as f:
                records=f.readlines()
                for line in records:
                    if int(line.strip().split()[0])==id:
                            print(line)
                            found=True
                            break
                            
            if found==False:
                print("Record not found")
        except FileNotFoundError:
            print("Record not found")
if __name__=="__main__":
    loop=1
    while loop:
        print(10*"*"+"Menu"+10*"*"+"\n1.Add Student Records \n2.View Student Records \n3.Search by Id \n4.Exit")
        ch=int(input("Enter A choice ::"))
        manager=StudentManager("students.txt")
        if ch<=4:
            match ch:
                case 1:
                    manager.addRecords()
                case 2:
                    manager.viewRecords()
                case 3:
                    manager.searchId()
                case 4:
                    loop=0
        else:
            print("Enter Valid Choice ::")
        print(25*"*")     

        
            

