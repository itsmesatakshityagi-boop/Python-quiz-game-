score = 0

print("===== QUIZ APPLICATION =====")

questions = [
["What is the capital of India?", "Delhi"],
["How many days are there in a week?", "7"],
["Which programming language are you learning?", "Python"],
["What is 2 + 2?", "4"],
["National animal of India?", "Tiger"],
["National bird of India?","Peacock"],
["How amny months are there in a year ?","12"],
["Largest planet in ouir solar system","Jupiter"],
["Who wrote Ramayana ","Valmiki"],
["What is the chemical symbol of water ","H20"]
]

for q in questions:
 answer=input(q[0]+":")

 if answer.lower()==q[1].lower():
  print("Correct!")
  score+=1
 else:
  print("Wrong!Correct Answer:",q[1])

print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
 print("Excellent!")
elif percentage >= 60:
 print("Good Job!")
else:
 print("Keep Practicing!")