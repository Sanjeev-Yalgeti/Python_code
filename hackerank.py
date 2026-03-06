# S=input("Enter String :").upper()
# vowcount=0
# constcount=0
# for i in S:
#     if i in "AEIOU":
#         string=i
#         for j in S[S.index(i):-1]:
#             string+=j
#             vowcount+=1
#     elif i in "QWRTYPSDFGHJKLZXCVBNM":
#         string=i
#         for j in S[S.index(i):-1]:
#             string+=i
#             constcount+=1
# result=f"Stuart {vowcount}" if vowcount>constcount else "Kevin {constcount}" 
# print(result)

#---------------------------------------------------------------------

# def merge_the_tools(string, k):
#     l=len(string)
#     for i in range(0,l,k):
#         sliced=string[i:i+k]
#         prev_j=""
#         for j in sliced:
#             if j not in prev_j:
#                 prev_j+=j
#         print(prev_j)
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# parCount=0
# rectCount=0
# curlyCount=0
# for i in stack:
#     if i=="{":
#         curlyCount-=1
#     elif i=="}":
#         curlyCount+=1
#     elif i==")":
#         parCount-=1
#     elif i=="(":
#         parCount+=1
#     elif i=="[":
#         rectCount+=1
#     elif i=="]":
#         rectCount-=1
# if(curlyCount==0 and parCount==0 and rectCount==0 ):
#     print("Balanced")
# else:
#     print("UnBalanced")



string = input("Enter string: ")

stack = []

for ch in string:
    if ch in "{([":
        stack.append(ch)
    elif ch in "})]":
        if not stack:
            print("Unbalanced")
            exit()
        top = stack.pop()
        if (ch == '}' and top != '{') or \
           (ch == ')' and top != '(') or \
           (ch == ']' and top != '['):
            print("Unbalanced")
            exit()

