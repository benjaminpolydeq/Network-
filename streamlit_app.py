import streamlit as st
from db.database import init_db, SessionLocal
from db.crud import create_contact, get_contacts
from utils.security import encrypt, decrypt

# INIT
init_db()
db = SessionLocal()

st.set_page_config(
    page_title="Network",
    page_icon="🧠",
    layout="wide"
)

st.title("📇 Network — Agenda Intelligent de Networking")

# SESSION STATE
if "saved" not in st.session_state:
    st.session_state.saved = False

# FORM
with st.form("add_contact", clear_on_submit=True):
    st.subheader("➕ Ajouter un contact")
    name = st.text_input("Nom")
    contact_info = st.text_input("Contact")
    domain = st.text_input("Domaine")
    occasion = st.text_input("Occasion")
    topics = st.text_area("Sujets abordés")
    next_action = st.text_input("Prochaine action")
    submitted = st.form_submit_button("Enregistrer")

    if submitted and name:
        create_contact(db, {
            "name": encrypt(name),
            "contact_info": encrypt(contact_info),
            "domain": domain,
            "occasion": occasion,
            "topics": topics,
            "next_action": next_action
        })
        st.session_state.saved = True

# MESSAGE APRÈS RERUN
if st.session_state.saved:
    st.success("✅ Contact enregistré avec succès")
    st.session_state.saved = False

# LISTE CONTACTS
st.divider()
st.subheader("📂 Contacts enregistrés")

contacts = get_contacts(db)

for c in contacts:
    with st.expander(decrypt(c.name)):
        st.write("📞 Contact :", decrypt(c.contact_info))
        st.write("🏷️ Domaine :", c.domain)
        st.write("🤝 Occasion :", c.occasion)
        st.write("📝 Sujets :", c.topics)
        st.write("🎯 Prochaine action :", c.next_action)