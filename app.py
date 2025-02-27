import streamlit as st
from PIL import Image

def calculate_heart_health(answers):
    try:
        age = int(answers.get("Ηλικία:", 0))
        weight = float(answers.get("Βάρος (kg):", 0))
        height = float(answers.get("Ύψος (m):", 1))
        bmi = weight / (height ** 2)
        bmi_text = f"ΔΜΣ: {bmi:.2f}"
        
        health_score = 100  # Μπορείς να προσθέσεις πιο σύνθετο υπολογισμό εδώ
        return bmi_text, f"Ποσοστό υγείας καρδιάς: {health_score:.2f}%"
    except ValueError:
        return None, "Παρακαλώ εισάγετε έγκυρες αριθμητικές τιμές."

# Ρύθμιση της εφαρμογής
st.set_page_config(page_title="Υγεία Καρδιάς", layout="centered")

# Προσθήκη εικόνας φόντου
st.image("heart_health.jpg", use_column_width=True)

st.title("Ερωτηματολόγιο Υγείας Καρδιάς")

questions = [
    ("Ηλικία:", "number"),
    ("Βάρος (kg):", "number"),
    ("Ύψος (m):", "number"),
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

for question in questions:
    q_text, q_type = question[0], question[1]
    if q_type == "number":
        answers[q_text] = st.number_input(q_text, min_value=0.0, step=1.0, format="%.2f")
    elif q_type == "choices":
        answers[q_text] = st.selectbox(q_text, question[2])

if st.button("Υπολογισμός Υγείας Καρδιάς"):
    bmi_result, health_result = calculate_heart_health(answers)
    if bmi_result:
        st.success(bmi_result)
        st.success(health_result)
    else:
        st.error(health_result)
