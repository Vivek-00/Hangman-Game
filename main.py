import random as ra
list1=['apple','banana','orange','pineapple','guava']
word=(ra.choice(list1))
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
		
	
