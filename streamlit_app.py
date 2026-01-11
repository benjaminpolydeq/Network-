import streamlit as st
from db import Session, Contact, Interaction
from ai_engine import analyse_discussion
from datetime import datetime

session = Session()

st.title("Agenda CRM Personnel + IA")

menu = st.sidebar.selectbox("Menu", ["Contacts", "Interactions", "Analyse IA"])

if menu == "Contacts":
    st.subheader("Gérer Contacts")
    name = st.text_input("Nom")
    email = st.text_input("Email")
    phone = st.text_input("Téléphone")
    domain = st.text_input("Domaine")
    if st.button("Ajouter"):
        c = Contact(name=name, email=email, phone=phone, domain=domain)
        session.add(c); session.commit()
        st.success("Contact ajouté !")

    contacts = session.query(Contact).all()
    for c in contacts:
        st.write(f"{c.id} | {c.name} | {c.email} | {c.phone} | {c.domain}")

elif menu == "Interactions":
    st.subheader("Ajouter Interaction")
    all_contacts = session.query(Contact).all()
    pick = st.selectbox("Choisir Contact", all_contacts, format_func=lambda c: c.name)

    notes = st.text_area("Notes de Discussion")
    if st.button("Enregistrer Interaction"):
        result = analyse_discussion(notes)
        inter = Interaction(
            contact_id=pick.id,
            date=datetime.now(),
            notes=notes,
            summary=result["summary"],
            important=("High" in result["importance"])
        )
        session.add(inter); session.commit()
        st.success("Interaction analysée & stockée !")
        st.write("🏷 Résumé :", result["summary"])
        st.write("⭐ Importance :", result["importance"])
        st.write("👉 Prochaines actions :", result["next_actions"])

elif menu == "Analyse IA":
    st.subheader("Visualiser Interactions Marquantes")
    interactions = session.query(Interaction).filter(Interaction.important == True).all()
    for i in interactions:
        st.write("---")
        st.write(f"📅 {i.date} — {i.summary}")