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
    