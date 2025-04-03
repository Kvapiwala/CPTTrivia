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
            option_buttons[i].pack(pady=5)
            option_buttons[i].config(text=option, command=lambda q=QSearch, Idx=i :check_answer(q, Idx)) #AI was used to debug the lambda

     
def check_answer(QSearch, AnsIndex):
        global score
        global Qindex

        selected_answer = QSearch["options"][AnsIndex]
        if selected_answer == QSearch["answer"]:
            answer_label.config(text="Correct!")
            score += 1
        else: 
            answer_label.config(text="Incorrect!")
            
        Qindex += 1
        root.after(1500, hide_label) #This line was added by ChatGPT

        if Qindex < len(Trivia):
            run_QandO(Trivia)
            SLabel.config(text= f"Your current score: {score} points.", font=("Arial", 12))
        else:
            SLabel.config(text=f"You finished the quiz! Your final score is: {score} out of 8 points or {(score/8)*100}%! ", font=("Arial", 14, "bold"))
            answer_label.config(text= "")
            for i in range (4):
                option_buttons[i].pack_forget()

            begin_game_btn.pack()
            begin_game_btn.config(text = "Play Again?")
            Qlabel.config(text= "")
            Qindex = 0
            score = 0

#ChatGPT Start
def hide_label():
    answer_label.config(text="")
#ChatGPT End

root = tk.Tk()
root.title("World Geography Quiz")
frame = tk.Frame(root, bg="#1e90ff")
frame.pack()
root.geometry("600x400")
root.configure(bg="#1e90ff")

SLabel = tk.Label(root, text = "", font=("Arial", 12), bg="#1e90ff", fg="#333333")
SLabel.pack(pady=5)


Qlabel = tk.Label(root, text = "", font=("Arial", 14, "bold"), bg="#1e90ff", fg= "#333333")
Qlabel.pack(pady=10)


#chatgpt start
option_buttons = []
for i in range(4):
    Obutton = tk.Button(root, text = "", font=("Arial", 12), bg="#cfb53b")
    option_buttons.append(Obutton)
#chatgpt end

answer_label = tk.Label(root, text = "", font=("Arial", 12), bg="#1e90ff")
answer_label.pack(pady=10)

begin_game_btn = tk.Button(frame, text= "Start Game", command=lambda:run_QandO(Trivia), font=("Arial", 12, "bold"), bg="#cfb53b")
begin_game_btn.pack(pady=5)


root.mainloop()
