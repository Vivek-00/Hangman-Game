import random
import pycorpora
print("Available categories\n""1.Flowers \n2.Fruits\n3.Music Instrumets\n")
userChoice=int(input("Enter a category: "))
if  userChoice==1:
    word=random.choice(pycorpora.plants.flowers["flowers"])
elif  userChoice==2:
    word=random.choice(pycorpora.foods.fruits["fruits"])
elif userChoice==3:
    word=random.choice(pycorpora.music.instruments
["instruments"])
else:
    pass
print(word)
print("It is a ",len(word)," letter word")
x=len(word)
y='*'
temp=y*x
print(len(temp))
print(y*x)
lives=10
live=100
for i in range(live):
    print("lives=",lives)
    if lives==0:
        print("Game Over")
        print("The correct word is",word)
        break
    if temp==word:
        print("You win")
        break
    ans=input("Enter the letter:")
    if ans in temp:
        print("Already entered")
    for j in range(0,len(word)):
        if word[j]==ans:
            temp=temp[:j]+ans+temp[j+1:]
            temp2=temp
            continue
    print(temp)
    if ans in word:
        lives=lives
    else:
        lives=lives-1
