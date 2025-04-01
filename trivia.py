import tkinter as tk

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
        "answer": "Germany"
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
    },
    {
        "questions": "What the largest city in the United States?",
        "options": ["Los Angeles", "Houston", "New York City", "Miami"],
        "answer": "New York City"
    },
    {
        "questions": "What Country is NOT part of North America",
        "options": ["United States", "Panama", "Mexico", "Canada"],
        "answer": "Panama"
    }
]


score = 0
QSearch = ""
Qindex = 0
AnsIndex = 0

def run_QandO(Trivia):
    global score
    global QSearch
    
    begin_game_btn.pack_forget()

    if Qindex < len(Trivia):
        QSearch = Trivia[Qindex]
        Qlabel.config(text=QSearch["questions"])
        
        for i, option in enumerate(QSearch["options"]):
            AnsIndex = i
            option_buttons[i].pack()
            option_buttons[i].config(text=option, command=lambda q=QSearch, Idx=i :check_answer(q, Idx)) #AI was used to debug the lambda

     
def check_answer(QSearch, AnsIndex):
        global score
        global Qindex

        correct_answer = QSearch["options"][AnsIndex]
        if correct_answer == QSearch["answer"]:
            answer_label.config(text="Correct!")
            score += 1
        else: 
            answer_label.config(text="Incorrect!")
            
        Qindex += 1

        if Qindex < len(Trivia):
            run_QandO(Trivia)
        else:
            answer_label.config(text=f"You finished the quiz! Your final score is: {score} points!")
            for i in range (4):
                option_buttons[i].pack_forget()

            begin_game_btn.pack()
            begin_game_btn.config(text = "Play Again?")
            Qlabel.config(text= "")
            Qindex = 0
            score = 0


root = tk.Tk()
root.title("World Geography Quiz")
frame = tk.Frame(root)
frame.pack()


Qlabel = tk.Label(root, text = "")
Qlabel.pack()

#chatgpt start
option_buttons = []
for i in range(4):
    Obutton = tk.Button(root, text = "")
    option_buttons.append(Obutton)
#chatgpt end

answer_label = tk.Label(root, text = "")
answer_label.pack()

begin_game_btn = tk.Button(frame, text= "Start Game", command=lambda:run_QandO(Trivia))
begin_game_btn.pack()


root.mainloop()