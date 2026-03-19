class Product:
    def __init__(self,pid,pname,stock,price):
        self.pid=pid
        self.pname=pname
        self.stock=stock
        self.price=price

    def to_string(self):
        return f"{self.pid} {self.pname} {self.stock} {self.price}"

class ProductManager:
    def __init__(self,filename):
        self.filename=filename

    def addRecords(self):
        pid=input("Enter Product ID :")
        pname=input("Enter Product name :")
        stock=int(input("Enter Stock Quantity :"))
        price=int(input("Enter price:"))
        s1=Product(pid,pname,stock,price)
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
        id=input("Enter Id to be searched :")
        try:
            found=False
            with open(self.filename,"r") as f:
                records=f.readlines()
                for line in records:
                    if line.strip().split()[0]==id:
                            print(line)
                            found=True
                            break
            if found==False:
                print("Record not found")
        except FileNotFoundError:
            print("Record not found")
    def update(self):
        try:
            with open(self.filename,"a+") as f:
                records=f.readlines()
                updatedFile=[]
                update_id=input("Enter Product Id to be updated :")
                new_qty=int(input("Enter Updated Product Quantity :"))
                for line in records:
                    if line[0] == update_id:
                        updatedFile.append(f"{line[0]} {line[1]} {line[2]} {new_qty}\n")
                    else:
                        updatedFile.append(line)
                for i in updatedFile:
                    f.write(i)
        except FileNotFoundError:
            print("File Not Found")
if __name__=="__main__":
    loop=1
    while loop:
        print(10*"*"+"Menu"+10*"*"+"\n1.Add Product Records \n2.View Product Records \n3.Search product  \n4.Update Quantity \n5.Exit")
        ch=int(input("Enter A choice ::"))
        manager=ProductManager("products.txt")
        if ch<=5:
            match ch:
                case 1:
                    manager.addRecords()
                case 2:
                    manager.viewRecords()
                case 3:
                    manager.searchId()
                case 4:
                    manager.update()
                case 5:
                    break
        else:
            print("Enter Valid Choice ::")
        print(25*"*")     

        
            


