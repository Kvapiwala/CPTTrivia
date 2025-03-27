import tkinter as tk
import tkinter.scrolledtext as tksc

Trivia = [
    {
        "questions": "What Country is Paris located in?",
        "options": ["United Kingdom", "United States", "Germany", "France"],
        "answer": "France"
    },
    {
        "questions": "What is the capital of Romania?",
        "options": ["Bucharest", "Sibiu", "Dej", "Oradea"],
        "answer": "Bucharest"
    },
    {
        "questions": "What continent is Ghana located in?",
        "options": ["North America", "South America", "Asia", "Africa"],
        "answer": "Africa"
    },
    {
        "questions": "What country does France share its longest land border with?",
        "options": ["United States", "Germany", "Brazil", "Africa"],
        "answer": "Africa"
    },
    {
        "questions": "What is considered the country that never gets dark?",
        "options": ["Norway", "Sweden", "Poland", "Finland"],
        "answer": "Finland"
    },
    {
        "questions": "What is a city in Brazil?",
        "options": ["Salvador", "Puebla", "Monterrey", "Bilbao"],
        "answer": "Salvador"
    }
]


score = 0


def run_QandO(trivia):
    global score

    for q in trivia:
        print(q["questions"])
        for i, option in enumerate(q["options"]):
            print(f"{i+1}. {option}")

        while True:
            try:
                answer = int(input("Enter your answer: ")) - 1
                if answer > 3:
                    raise ValueError
                break
            except ValueError:
                print("enter in a number in range from 1-4")

        correct_answer = q["options"][answer]
        if correct_answer == q["answer"]:
            print("Correct!")
            score += 1
        else: 
            print("Incorrect!")
        print(f"Your final score was {score} points Good job!")

root = tk.Tk()
root.title("World Geography Quiz")
frame = tk.Frame(root)
frame.pack()

begin_game_btn = tk.Button(frame, text= "Start Game", command=lambda:run_QandO(Trivia))
begin_game_btn.pack()

Qlabel = tk.Label(root, text = "")
Qlabel.pack()

#chatgpt start
option_buttons = []
for i in range(4):
    Obutton = tk.Button(root, text = "")
    Obutton.pack()
    option_buttons.append(Obutton)
#chatgpt end

answer_label = tk.Label(root, text = "")

root.mainloop()