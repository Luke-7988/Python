import random
ans=random.randint(1,20)
i=0
while i<5:
    num=int(input('input a num'))
    if num>ans:
        print("your answer is too big")
    elif num<ans:
        print("your number is too small")
    else:
        print("you played", i+1, "times")
        break
    i=i+1
