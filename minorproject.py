from tkinter import *
from random import randint, choice  #choice choose a random value from given list or tuple

root = Tk()   #ui
root.geometry("600x600")   #window size
root.title("Maths Quiz")   

headingLabel = Label(root, text="Maths Quiz", font=('times new roman', 20)) #label represent on the screen
headingLabel.grid(row=0, column=0)  #grid help to know where label is displayed

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionCount = IntVar()

questionLabel = Label(root, text="", font=('times new roman', 17))
questionLabel.grid(row=1, column=0) 

def generateQuestion():   #generate randomly question whenever function is call
    if questionCount.get() >= 10:  #stop after 10 questions
        questionLabel.config(text="Quiz Completed!")
        return
    
    number1 = randint(1, 10)  #randint=random number generate between 1 to 10
    number2 = randint(1, 10)
    
    operator = choice(['+', '-', '*', '//'])  
    
    question.set(str(number1) + operator + str(number2))  #put value in question
    answer.set(str(eval(question.get())))  #eval evaluates our question and gives the answer

    questionLabel.config(text=question.get())  

def checkAnswer():  
    if questionCount.get() < 10: 
        if str(answer.get()) == givenAnswer.get():
            print("correct")
            resultLabel.config(text="correct", fg="green", bg="sky blue")
            score.set(score.get()+1)       #set is for new value of score
            scoreLabel.config(text=f"Score:{score.get()}")  
        else:
            print("incorrect")
            resultLabel.config(text="incorrect", fg="red", bg="sky blue")
        
        questionCount.set(questionCount.get() + 1)  #increase count
        progressLabel.config(text=f"Question: {questionCount.get()}/10")  #update progress

        givenAnswer.set("")  
        generateQuestion()  
def restartQuiz():  
    score.set(0)  
    questionCount.set(0)  
    givenAnswer.set("")  
    resultLabel.config(text="Result", fg="blue", bg=root.cget("bg"))  
    scoreLabel.config(text=f"Score:{score.get()}")  
    progressLabel.config(text="Question: 0/10")  
    generateQuestion()

generateQuestion()  

#user interface
answerEntry = Entry(root, textvariable=givenAnswer, font=('arial', 16))  
answerEntry.grid(row=2, column=0) 

submitButton = Button(root, text="Submit", font=('times new roman', 14), command=checkAnswer)
submitButton.grid(row=2, column=1) 

restartButton = Button(root, text="Restart", font=('times new roman', 14), command=restartQuiz)  #restart button
restartButton.grid(row=5, column=0)

resultLabel = Label(root, text="Result", font=('times new roman', 17), fg="blue")
resultLabel.grid(row=3, column=0)

scoreLabel= Label(root, text=f"Score:{score.get()}", font=('times new roman', 17), fg="black")
scoreLabel.grid(row=4, column=0)

progressLabel = Label(root, text="Question: 0/10", font=('times new roman', 17), fg="black")  
progressLabel.grid(row=6, column=0)

print(question.get())
print(answer.get())

root.mainloop()
