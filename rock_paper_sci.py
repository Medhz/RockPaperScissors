choice=int(input("what do you choose? type 0 for rock ,1 for paper and 2 for scissors  "))
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lis=[rock,paper,scissors]
print(lis[choice])
com=random.randint(0,2)
print(f"computer choose:{com}")
if com==0:
  print(rock)
elif com==1:
  print(paper)
else :
  print(scissors) 

if choice==0 and com!=0:
  if com!=1:
   print("you win 😉")
  else:
   print("you loose 😟")
elif choice==1 and com!=1:
  if com!=2:
   print("you win😉 ")
  else:
   print("you loose😟")
elif choice==2 and com!=2:
  if com!=0:
   print("you win 😉")
  else:
   print("you loose 😟")  
else:
  print("draw")    

 
       

