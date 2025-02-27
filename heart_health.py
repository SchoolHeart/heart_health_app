import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

questions = [
    ("Ηλικία:", "entry"),
    ("Βάρος (kg):", "entry"),
    ("Ύψος (m):", "entry"),
    ("Έχετε υψηλή αρτηριακή πίεση;", "choices", ["Όχι", "Μέτρια", "Υψηλή"]),
    ("Έχετε υψηλή χοληστερίνη;", "choices", ["Όχι", "Μέτρια", "Υψηλή"]),
    ("Καπνίζετε;", "choices", ["Όχι", "Λίγο", "Πολύ"]),
    ("Ακολουθείτε ανθυγιεινή διατροφή;", "choices", ["Όχι", "Μερικές φορές", "Συχνά"]),
    ("Ζείτε σε περιοχή με ρύπανση;", "choices", ["Όχι", "Μέτρια", "Υψηλή"]),
    ("Έχετε έκθεση σε θόρυβο;", "choices", ["Όχι", "Μέτρια", "Υψηλή"]),
    ("Αισθάνεστε μοναξιά;", "choices", ["Όχι", "Μερικές φορές", "Συχνά"]),
    ("Αντιμετωπίζετε συναισθηματικές δυσκολίες;", "choices", ["Όχι", "Μερικές φορές", "Συχνά"])
]

answers = {}
current_question = 0

def next_question():
    global current_question
    if current_question > 0:
        if questions[current_question - 1][1] == "entry":
            answers[questions[current_question - 1][0]] = entry_var.get()
        else:
            answers[questions[current_question - 1][0]] = choice_var.get()
    
    if current_question < len(questions):
        question_label.config(text=questions[current_question][0])
        
        if questions[current_question][1] == "entry":
            entry_var.set("")
            entry.grid(row=1, column=1)
            choice_menu.grid_forget()
        else:
            choice_var.set(questions[current_question][2][0])
            entry.grid_forget()
            choice_menu.grid(row=1, column=1)
        
        current_question += 1
    else:
        calculate_heart_health()

def calculate_heart_health():
    try:
        age = int(answers["Ηλικία:"])
        weight = float(answers["Βάρος (kg):"])
        height = float(answers["Ύψος (m):"])
        bmi = weight / (height ** 2)
        bmi_text = f"ΔΜΣ: {bmi:.2f}"
        
        messagebox.showinfo("Αποτέλεσμα", bmi_text)
        
        health_score = 100  # (Υπολογισμός όπως πριν)
        
        messagebox.showinfo("Αποτέλεσμα", f"Ποσοστό υγείας καρδιάς: {health_score:.2f}%")
    except ValueError:
        messagebox.showerror("Σφάλμα", "Παρακαλώ εισάγετε έγκυρες αριθμητικές τιμές.")

app = tk.Tk()
app.title("Υγεία Καρδιάς")
app.geometry("500x400")
app.configure(bg="black")

bg_image = Image.open("heart_health.jpg")  # Προσθήκη εικόνας φόντου
bg_image = bg_image.resize((500, 400))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(app, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

question_label = tk.Label(app, text="", font=("Arial", 14), bg="black", fg="white")
question_label.grid(row=0, column=1, pady=20)

entry_var = tk.StringVar()
entry = tk.Entry(app, textvariable=entry_var, font=("Arial", 12))

choice_var = tk.StringVar()
choice_menu = tk.OptionMenu(app, choice_var, "")
choice_menu.config(font=("Arial", 12))

next_button = tk.Button(app, text="Επόμενο", command=next_question, font=("Arial", 12), bg="red", fg="white")
next_button.grid(row=2, column=1, pady=20)

next_question()

app.mainloop()
