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
QSearch = ""
Qindex = 0
AnsIndex = 0

def run_QandO(trivia):
    global score
    global QSearch
    
    if Qindex < len(Trivia):
        q = Trivia[Qindex]
        QSearch = q
        Qlabel.config(text=q["questions"])
        
        print(q["questions"])
        for i, option in enumerate(q["options"]):
            AnsIndex = i
            option_buttons[i].config(text=option, command=lambda q=QSearch, Idx=i :check_answer(q, Idx)) #AI was used to debug the lambda
            print(f"{i+1}. {option}")

     
def check_answer(QSearch, AnsIndex):
        global score
        
        correct_answer = QSearch["options"][AnsIndex]
        if correct_answer == QSearch["answer"]:
            answer_label.config(text="Correct!")
            score += 1
        else: 
            answer_label.config(text="Incorrect!")
        
        AnsIndex += 1
        Qindex += 1



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
    Obutton.pack()
    option_buttons.append(Obutton)
#chatgpt end

answer_label = tk.Label(root, text = "")
answer_label.pack()

begin_game_btn = tk.Button(frame, text= "Start Game", command=lambda:run_QandO(Trivia))
begin_game_btn.pack()

root.mainloop()