import tkinter as tk
from tkinter import messagebox

# List of questions, options, and correct answers
questions = [
    ("What is the keyword to define a function in Python?", ["def", "function", "define", "fun"], "def"),
    ("Which operator is used for exponentiation in Python?", ["^", "**", "//", "%"], "**"),
    ("Which of the following is a mutable data type?", ["list", "tuple", "string", "int"], "list"),
    ("What is the correct extension of a Python file?", [".py", ".pyt", ".python", ".pt"], ".py"),
    ("What is the result of 5 // 2 in Python?", ["2", "2.5", "3", "None of the above"], "2"),
    ("Which function is used to get the length of an object in Python?", ["len()", "length()", "size()", "count()"], "len()"),
    ("What is the output of print(2 * '3')?", ["6", "33", "23", "None of the above"], "33"),
    ("How do you start a block of code in Python?", ["{", ":", "(", "["], ":"),
    ("Which of the following is a valid tuple?", ["(1, 2)", "[1, 2]", "{1, 2}", "(1, 2, 3, )"], "(1, 2, 3,)"),
    ("What is the default value of the argument in a function if not specified?", ["None", "0", "False", "empty string"], "None")
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ayush's Python Quiz App")
        
        self.score = 0
        self.question_index = 0
        self.selected_option = tk.StringVar()
        
        self.create_widgets()
        self.show_question()
    
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("Helvetica", 18), width=25, height=2, indicatoron=0, bg="lightblue", activebackground="lightgreen")
            button.pack(pady=10)
            self.option_buttons.append(button)
        
        # Next Button (Stylized differently)
        self.next_button = tk.Button(self.root, text="Next", font=("Helvetica", 16), command=self.next_question, width=20, height=2, bg="blue", fg="white", activebackground="green")
        self.next_button.pack(pady=20)
        
        # Submit Button (Stylized differently)
        self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 16), command=self.submit_quiz, width=20, height=2, bg="red", fg="white", activebackground="darkred")
        self.submit_button.pack(pady=20)
    
    def show_question(self):
        question, options, _ = questions[self.question_index]
        self.question_label.config(text=question)
        
        for i in range(4):
            self.option_buttons[i].config(text=options[i], value=options[i])
        
        self.selected_option.set("")  # Reset the selected option
    
    def next_question(self):
        answer = self.selected_option.get()
        correct_answer = questions[self.question_index][2]
        
        if answer == correct_answer:
            self.score += 1
        
        self.question_index += 1
        
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.submit_quiz()  # Submit the quiz when all questions are answered
    
    def submit_quiz(self):
        messagebox.showinfo("Quiz Completed", f"Your total score is: {self.score}/{len(questions)}")
        self.root.quit()

# Create the main window and start the quiz
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()


