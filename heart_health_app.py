import streamlit as st
from PIL import Image

# Ορισμός των ερωτήσεων
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

# Εμφάνιση εικόνας φόντου
bg_image = Image.open("heart_health.jpg")  # Βεβαιώσου ότι η εικόνα υπάρχει στο directory
st.image(bg_image, use_column_width=True)

# Υπολογισμός υγείας καρδιάς
def calculate_heart_health():
    try:
        age = int(answers["Ηλικία:"])
        weight = float(answers["Βάρος (kg):"])
        height = float(answers["Ύψος (m):"])
        bmi = weight / (height ** 2)
        bmi_text = f"ΔΜΣ: {bmi:.2f}"
        
        st.write(bmi_text)
        
        health_score = 100  # (Υπολογισμός όπως πριν)
        
        st.write(f"Ποσοστό υγείας καρδιάς: {health_score:.2f}%")
    except ValueError:
        st.error("Παρακαλώ εισάγετε έγκυρες αριθμητικές τιμές.")

# Εμφάνιση ερωτήσεων και καταγραφή απαντήσεων
def ask_questions():
    for question in questions:
        if question[1] == "entry":
            answer = st.text_input(question[0])
            if answer:
                answers[question[0]] = answer
        else:
            answer = st.selectbox(question[0], question[2])
            answers[question[0]] = answer

# Εξακρίβωση και εμφάνιση αποτελέσματος
st.title("Υγεία Καρδιάς")

ask_questions()

if len(answers) == len(questions):
    if st.button('Υπολογισμός Υγείας Καρδιάς'):
        calculate_heart_health()
