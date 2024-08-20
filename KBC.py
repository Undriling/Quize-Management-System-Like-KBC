questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  ]

levels=[1000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,5000000,10000000,20000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for rupees: ₹{levels[i]}/-")
    print(f"{question[0]}")
    print(f"1. {question[1]}           2.{question[2]}")
    print(f"3. {question[3]}           4.{question[4]}")
    reply=int(input("Enter your answer between 1 to 4 :- "))
    if reply==question[-1]:
        print(f"Correct answer! Your wining amt. is:- ₹{levels[i]}/-")
        if i==4:
            money=20000
        elif i==9:
            money=640000
        elif i==12:
            money=20000000
            break
    else:
        print("Wrong answer.")
        break
print(f"Congrats! You will go home with ₹{money}/-")



