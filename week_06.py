def jaccard_similarity (set1, set2):
    return (len(set.intersection(set1,set2))/len(set.union(set1,set2)))

def find_most_similar_user(users, target_user):
    most=0
    for i in users:
        if(target_user==i): 
            continue
        js=jaccard_similarity(users[i],users[target_user])
        print(f"Similarity with {i}:  {js}")
        if(js>most):
            most=js
            most_sim_user=i
    return most_sim_user,most

def recommend_products(users, target_user, similar_user):
    recommed=set.difference(users[similar_user],users[target_user])
    return recommed
if __name__ == "__main__":
    users = {
        "U1": {"P101", "P102", "P103"},
        "U2": {"P102", "P103", "P104", "P105"},
        "U3": {"P106", "P107"},
        "U4": {"P101", "P103", "P104"}
    }
target_user = "U1"
similar_user,score=find_most_similar_user(users,target_user)
recommend=recommend_products(users,target_user,similar_user)
print(f"Most Similar User {similar_user}")
print(f"Most highest jaccard Similarity:{score}")
print(f"Reccomendation:{recommend}")
# Find most similar user
# Recommend products
# Display similarity scores and recommendations