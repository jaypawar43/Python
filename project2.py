import random
def gameplay(comp,user):
    if comp==user:
        return None
    elif comp== "stone":
        if user== "paper":
            return 
        elif user== "scissor":
            return False
    elif comp== "paper":
        if user== "scissor":
            return True
        elif user== "stone":
            return False    
    elif comp== "scissor":
        if user== "paper":
            return False
        elif user== "stone":
            return True    
print("computer had choosen")
rando= random.randint(1,3)
if rando==1:
    comp="stone"
elif rando==2:
    comp="scissor"
elif rando==3:
    comp="paper"
user=input("user's turn: \n")        
a=gameplay(comp,user)
if a==None:
    print("The match has been tie")
elif a:
    print("you win")
else:
    print("you lose")  