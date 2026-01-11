import streamlit as st
from db.database import SessionLocal, init_db
from db import crud
from ai.nlp_analysis import analyze_conversation
from utils.notifications import notify
from utils.security import encrypt, decrypt

# Init DB
init_db()
db = SessionLocal()

st.set_page_config(page_title="Network", page_icon="🗂️", layout="wide")

st.title("Network - Agenda de Networking Intelligent")

# Ajouter un contact
with st.form("add_contact"):
    st.subheader("Ajouter un contact")
    name = st.text_input("Nom")
    contact_info = st.text_input("Contact")
    domain = st.text_input("Domaine")
    occasion = st.text_input("Occasion")
    topics = st.text_area("Sujets abordés")
    next_action = st.text_input("Prochaine action")
    rendez_vous = st.date_input("Rendez-vous")
    submitted = st.form_submit_button("Ajouter")
    
    if submitted:
        data = {
            "name": encrypt(name),
            "contact_info": encrypt(contact_info),
            "domain": domain,
            "occasion": occasion,
            "topics": topics,
            "next_action": next_action,
            "rendez_vous": str(rendez_vous)
        }
        crud.create_contact(db, data)
        notify("Contact ajouté avec succès!")

# Afficher contacts
st.subheader("Mes contacts")
contacts = crud.get_contacts(db)
for c in contacts:
    st.markdown(f"- **Nom:** {decrypt(c.name)}, **Domaine:** {c.domain}, **Prochaine action:** {c.next_action}")