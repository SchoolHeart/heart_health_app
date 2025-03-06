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

# Βάρη για κάθε κατηγορία (W)
weights = {
    "bio": 0.4,  # Βιολογικοί παράγοντες (ηλικία, βάρος, ύψος, αρτηριακή πίεση, χοληστερίνη)
    "soc": 0.1,  # Κοινωνικοί παράγοντες (καπνίζετε)
    "diet": 0.2,  # Διατροφή (ανθυγιεινή διατροφή)
    "env": 0.15,  # Περιβαλλοντικοί παράγοντες (ρύπανση, θόρυβος)
    "emo": 0.15   # Συναισθηματικοί παράγοντες (μοναξιά, συναισθηματικές δυσκολίες)
}

# Συνάρτηση για την αντιστοίχιση των απαντήσεων σε αριθμητικές τιμές (B)
def map_score(answer, options):
    if answer == options[0]:  # Όχι
        return 1.0
    elif answer == options[1]:  # Μέτρια/Λίγο/Μερικές φορές
        return 0.5
    elif answer == options[2]:  # Υψηλή/Πολύ/Συχνά
        return 0.0

# Εμφάνιση εικόνας φόντου
bg_image = Image.open("heart_health.jpg")  # Βεβαιώσου ότι η εικόνα υπάρχει στο directory
st.image(bg_image, use_column_width=True)

# Υπολογισμός υγείας καρδιάς
def calculate_heart_health():
    try:
        # Βιολογικοί παράγοντες (ηλικία, βάρος, ύψος, αρτηριακή πίεση, χοληστερίνη)
        age = int(answers["Ηλικία:"])
        weight = float(answers["Βάρος (kg):"])
        height = float(answers["Ύψος (m):"])
        bmi = weight / (height ** 2)
        bmi_text = f"ΔΜΣ: {bmi:.2f}"
        
        st.write(bmi_text)
        
        # Αντιστοίχιση απαντήσεων σε αριθμητικές τιμές
        blood_pressure_score = map_score(answers["Έχετε υψηλή αρτηριακή πίεση;"], ["Όχι", "Μέτρια", "Υψηλή"])
        cholesterol_score = map_score(answers["Έχετε υψηλή χοληστερίνη;"], ["Όχι", "Μέτρια", "Υψηλή"])
        smoking_score = map_score(answers["Καπνίζετε;"], ["Όχι", "Λίγο", "Πολύ"])
        diet_score = map_score(answers["Ακολουθείτε ανθυγιεινή διατροφή;"], ["Όχι", "Μερικές φορές", "Συχνά"])
        pollution_score = map_score(answers["Ζείτε σε περιοχή με ρύπανση;"], ["Όχι", "Μέτρια", "Υψηλή"])
        noise_score = map_score(answers["Έχετε έκθεση σε θόρυβο;"], ["Όχι", "Μέτρια", "Υψηλή"])
        loneliness_score = map_score(answers["Αισθάνεστε μοναξιά;"], ["Όχι", "Μερικές φορές", "Συχνά"])
        emotional_score = map_score(answers["Αντιμετωπίζετε συναισθηματικές δυσκολίες;"], ["Όχι", "Μερικές φορές", "Συχνά"])
        
        # Υπολογισμός του ποσοστού υγείας καρδιάς
        bio_score = (blood_pressure_score + cholesterol_score) / 2
        soc_score = smoking_score
        diet_score = diet_score
        env_score = (pollution_score + noise_score) / 2
        emo_score = (loneliness_score + emotional_score) / 2
        
        cardiac_health = 100 * (
            weights["bio"] * bio_score +
            weights["soc"] * soc_score +
            weights["diet"] * diet_score +
            weights["env"] * env_score +
            weights["emo"] * emo_score
        )
        
        st.write(f"Ποσοστό υγείας καρδιάς: {cardiac_health:.2f}%")
        
        # Εμφάνιση συμπεράσματος και πρότασης
        if cardiac_health >= 91:
            st.success("Εξαιρετική καρδιακή υγεία! Συνεχίστε με τις καλές συνήθειές σας.")
        elif cardiac_health >= 81:
            st.success("Πολύ καλή καρδιακή υγεία! Κρατήστε το επίπεδο και προσπαθήστε για ακόμα καλύτερα.")
        elif cardiac_health >= 71:
            st.info("Καλή καρδιακή υγεία. Υπάρχει χώρος για βελτίωση, αλλά είστε σε καλό δρόμο.")
        elif cardiac_health >= 61:
            st.warning("Μέτρια καρδιακή υγεία. Είναι σημαντικό να κάνετε αλλαγές στον τρόπο ζωής σας.")
        elif cardiac_health >= 51:
            st.warning("Μέτρια προς κακή καρδιακή υγεία. Χρειάζεται να λάβετε σοβαρά μέτρα για τη βελτίωση της υγείας σας.")
        elif cardiac_health >= 40:
            st.error("Κακή καρδιακή υγεία. Είναι σημαντικό να συμβουλευτείτε γιατρό και να κάνετε αλλαγές άμεσα.")
        else:
            st.error("Πολύ κακή καρδιακή υγεία. Χρειάζεται άμεση ιατρική παρέμβαση και αλλαγές στον τρόπο ζωής σας.")
            
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