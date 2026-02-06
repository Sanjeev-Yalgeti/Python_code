# #week 3
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# def is_krishnamurthy(num):
#     string=str(num)
#     sum_fact=0
#     for j in string:
#         ind_fact=factorial(int(j))
#         sum_fact+=factorial(int(j))
#        return sum_fact == num
#     if sum_fact==num:
#         print("True")
#     elif sum_fact!=num:
#         print("False")
# inp=int(input("Enter number :"))

# is_krishnamurthy(inp)

# #QUestion 2
# def apply_disount(price,discount=5):
#     final=price-(price*discount)/100
#     print("Discounted price:",final)
#Question 3
def dec_to_bin(dec):
    if dec==1 or dec ==0:
        return dec
    else:
        return str(dec_to_bin(dec//2))+str(dec%2)

print(dec_to_bin(10))