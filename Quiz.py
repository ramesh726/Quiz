questions=("Which is the largest planet in our solar system?: ",
           "Which country is famous for the Great Wall?:  ",
           "What is the capital of Australia?:  ",
           "Which continent has the most countries?: ")


options=(("A. Earth","B. Jupiter","C.Mars ","D.Venus "),
         ("A. India","B. China","C.Japan ","D.Mongolle "),
         ("A.Sydney","B.Melbourne","C.Canberra","D.Perth"),
         ("A. Asia","B.Africa ","C.Europe ","D.South Africa "))
answers=("A","B","C","B")
guesses=[]
score=0
question_num=0

for question in questions:
   print("----------------")
   print(question)
   for option in options[question_num]:
      print(option)
   guess=input("enter (A,B,C,D):").upper()
   guesses.append(guess)
   if guess ==answers[question_num]:
      score+=1
      print("CORRECT")
   else:
      print("incorrect")
      print(f"{answers[question_num]} is the correct answer")
   question_num +=1
print("-----------------------------")
print("          RESULTS            ")
print("-----------------------------")
print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f"your Score is:{score}%")