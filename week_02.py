# #Smart electricity bill calc
# unit=int(input("Enter consumed units: "))
# if(unit<=100):
#     cost=unit*1.5
#     print("Electricity Bill:",cost)
# elif(unit>100 and unit<=200):
#     cost=(100*1.5)+((unit-100)*2.5)
#     print("Electricity bill :",cost)
# elif(unit>200):
#     cost=(100*1.5)+(100*2.5)+(unit-200)*4
#     print("Electricity Bill:",cost)
#Digital Root calculator
# num=int(input("Enter Number :"))
# cpy=num
# over=False
# while over==False :
#     s=0
#     for i in str(cpy):
#         s=s+int(i)
#     if len(str(s))>1:
#         cpy=s
#     else:
#         over=True
# print(f"Digital root y{s} ")
# #aplhabet and pascals triangle
# row=int(input("Enter Number of rows"))
# s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(row):
#     s[]
#Leap year or noyt
year=int(input("Enter Year"))
if(year%4 == 0 and year%100 != 0  )or(year%400 == 0):
    print(f"{year} is a Leap Year")