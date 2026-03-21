class Employee():
    def __init__(self,rating,empid,name,basicSal):
        self.__rating=rating         
        self.__empid=empid
        self.__name=name
        self.__basicSal=basicSal
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self,rating):
        if 1<=rating<=5:
            self.__rating=rating
    @property
    def basicSal(self):
        return self.basicSal
    @basicSal.setter
    def basicSal(self,basicSal):
        if basicSal>0:
            self.__basicSal=basicSal

    def calculate_net_salary(self):
        match self.__rating:
            case 1:
                net_sal=self.__basicSal
            case 2:
                net_sal=self.__basicSal*0.05+self.__basicSal
            case 3:
                net_sal=self.__basicSal*0.10+self.__basicSal
            case 4:
                net_sal=self.__basicSal*0.15+self.__basicSal
            case 5:
                net_sal=self.__basicSal*0.2 +self.__basicSal 
        print(net_sal)
    def __str__(self):
        return f"Employee Id {empid} EMployee Name {name} Rating {rating} Basic Salary {basicSal}"
if __name__=="__main__":
    while True:
        ch=int(input("1.Add Employee \n 2.Calculate Net Salary \n 3.Display Employee Name \n 4.Exit \n Enter Your choice :"))
        if(ch==4):
            break
        match ch:
            case 1:
                empid=int(input("Enter Employee Id of employee :"))
                name=input("Enter name of employee :")
                basicSal=int(input("Enter Salary of employee :"))
                rating=int(input("Enter rating of employee :"))
                e=Employee(rating,empid,name,basicSal)
                print("Employee added Successfully ")
            case 2:
                e.calculate_net_salary()
            case 3:
                print(e)
