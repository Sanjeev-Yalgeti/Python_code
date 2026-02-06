#rotattion
# d=int(input("Enter D value :"))
# s=input("Enter String :")
# rot=input("Enter rotation type:(left/right):")
# if rot=="left":
#     temp=s[d:]
#     s=s[0:d]
#     temp=temp+s
#     print(temp)
# elif rot=="right":
#     temp=s[-1:-d-1]
#     s=s[:-d-1]
#     temp=temp+s
#     print(temp)
#----------------------------------------------------------------------------------
#Char counting and Validatipon
# lower,digit,special,upper=0,0,0,0
# p=input("Enter Password: ")
# for i in p:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace()==False:
#         special+=1
# print(f"Number of lowercase:{lower}\t Number of upper:{upper}\t Number of SPecial:{special}\t Number of digits:{digit}")

#------------------------------------------------------------------------------------------
#Socialk media Hashtag Exctracted
from string import punctuation
tweet=input("ENter Tweet  :")
tweet_list=tweet.split()
hashtag=[]
for i in tweet_list:
    if i[0]=="#":
        result="".join(c for c in i[1:] if c not in punctuation)
        hashtag.append(result)
print(hashtag)
