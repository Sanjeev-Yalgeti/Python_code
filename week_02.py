#Smart electricity bill calc
unit=int(input("Enter consumed units: "))
if(unit<=100):
    cost=unit*1.5;
    print("Electricity Bill:",cost)
elif(unit>100 and unit<=200):
    cost=(100*1.5)+((unit-100)*2.5)
    print("Electricity bill :",cost)
elif(unit>200):
    cost=(100*1.5)+(100*2.5)+(unit-200)*4
    print("Electricity Bill:",cost)
