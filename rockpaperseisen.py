import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Ener your choice {Rock , Paper, Scissor} = ")
comp_choice=random.choice(item_list)
print(f"User Choice = {user_choice} && Computer Choice = {comp_choice}")

if user_choice==comp_choice:
    print("Both chosses same match tie ")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers Rock ! Computer win ")
    else:
        print("Rock smashes Scissor ! You win ")
elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("Scissor cuts paper ! Computer win ")
    else:
        print("Paper covers Rock ! You win")
elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor cuts Paper ! You win ")
    else :
        print("Rock smashes Paper ! Computer win ")
        