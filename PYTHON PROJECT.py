#Python Quiz Game

Questions = ["1. how many minutes are in a full week?:",
             "2.what language is spoken in brazil?: ",
             "3.what is the most abundant gas in earth atmosphere",
             "4.how many hearts  does have an octopus have?:",
             "5.whats is the chemical symbol of gold?:"]

Options =[("A.  10,080",  "B.  10,180",  "C.  10,280",  "D.  10,380"),
          ("A.  Spanish",  "B.  Portuguese","C.  English", "D. French"),
          ("A.  Nitrogen",  "B.  OXygen", "C.  Carbon-Dioxide", "D.  Hydrogen"),
          ("A.  6",      "B.  5",   "C.  3",  "D.  2"),
          ("A.  Gd",     "B.  Go",  "C.  Ag",  "D.  Au")
           ]

Answers   = [ "A",  "B",  "A",  "C",   "D"]
Guesses =[]
Score=0
Question_num=0

for Question in Questions:
    print('------------------------------')
    print(Question)
    for Option in Options[Question_num]:
        print(Option)

    Guess = input("Enter a (A,B,C,D): ").upper()
    # Guesses.append(Guess)
    if Guess==Answers [Question_num]:
        Score+=1
        print('correct')
    else:
        print('Incorrect')
        print(f"{Answers[Question_num]} is the correct answer")

    Guesses.append(Guess)
    Question_num+=1

print("------------------------------------------")
print("                 Results                 ")
print("------------------------------------------")


print("Answers:",end=" ")
for Answer in Answers:
    print(Answer,end=" ")

print()

print("Guesses:",end=" ")
for Guess in Guesses:
    print(Guess,end=" ")
print()


Score=int(Score/ len(Questions)*100)
print(f"Your score is:{Score}%")


