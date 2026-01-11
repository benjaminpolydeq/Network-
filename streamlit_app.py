import streamlit as st
from db import init_db, SessionLocal
from models.contact import Contact
from models.interaction import Interaction
from chat_engine import add_message, get_messages
from ai_engine import analyze_discussion, synthesize_thread
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="networkIN", 
    page_icon="📒", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation DB
@st.cache_resource
def get_db():
    init_db()
    return SessionLocal()

db = get_db()

# En-tête principal
st.title("📒 networkIN")
st.caption("WhatsApp Business Intelligence - Gestion intelligente de vos contacts professionnels")

# Menu latéral avec style
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Choisir une section",
    [
        "➕ Ajouter Contact",
        "💬 Nouvelle Interaction",
        "🧵 Fil de discussion",
        "✍️ Signature Contact",
        "📊 Tableau de bord"
    ],
    label_visibility="collapsed"
)

# ===== AJOUTER CONTACT =====
if menu == "➕ Ajouter Contact":
    st.header("➕ Ajouter un nouveau contact")
    
    with st.form("add_contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Nom complet *", placeholder="Jean Dupont")
            email = st.text_input("Email", placeholder="jean.dupont@example.com")
            phone = st.text_input("Téléphone", placeholder="+33 6 12 34 56 78")
        
        with col2:
            domain = st.text_input("Domaine d'activité", placeholder="Technologie, Finance, etc.")
            context = st.text_area(
                "Contexte de rencontre", 
                placeholder="Conférence Tech Summit 2024, recommandé par...",
                height=100
            )
        
        submitted = st.form_submit_button("💾 Enregistrer le contact", use_container_width=True)
        
        if submitted:
            if not name:
                st.error("❌ Le nom est obligatoire")
            else:
                try:
                    c = Contact(
                        name=name, 
                        email=email, 
                        phone=phone, 
                        domain=domain, 
                        context=context
                    )
                    db.add(c)
                    db.commit()
                    st.success(f"✅ Contact '{name}' ajouté avec succès!")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Erreur lors de l'ajout: {str(e)}")
                    db.rollback()

# ===== NOUVELLE INTERACTION =====
elif menu == "💬 Nouvelle Interaction":
    st.header("💬 Enregistrer une nouvelle interaction")
    
    contacts = db.query(Contact).all()
    
    if not contacts:
        st.warning("⚠️ Aucun contact disponible. Veuillez d'abord ajouter un contact.")
    else:
        contact = st.selectbox(
            "Sélectionner un contact",
            contacts,
            format_func=lambda c: f"{c.name} ({c.domain or 'Sans domaine'})"
        )
        
        st.write(f"**Email:** {contact.email or 'Non renseigné'}")
        st.write(f"**Téléphone:** {contact.phone or 'Non renseigné'}")
        
        st.divider()
        
        discussion = st.text_area(
            "Discussion / Message",
            placeholder="Décrivez votre échange avec ce contact...",
            height=200
        )
        
        col1, col2 = st.columns([3, 1])
        
        with col2:
            analyze_btn = st.button("🧠 Analyser et Enregistrer", use_container_width=True)
        
        if analyze_btn:
            if not discussion.strip():
                st.error("❌ Veuillez entrer le contenu de la discussion")
            else:
                with st.spinner("🤖 Analyse en cours par l'IA..."):
                    try:
                        analysis = analyze_discussion(discussion)
                        
                        inter = Interaction(
                            contact_id=contact.id,
                            discussion=discussion,
                            summary=analysis,
                            key_points=analysis,
                            importance="High" if "high" in analysis.lower() else "Medium",
                            useful="oui" in analysis.lower() or "useful" in analysis.lower(),
                            next_action=analysis
                        )
                        db.add(inter)
                        db.commit()
                        
                        add_message(db, contact.id, discussion)
                        
                        st.success("✅ Interaction analysée et enregistrée!")
                        
                        st.markdown("### 🧠 Analyse IA de l'interaction")
                        st.info(analysis)
                        
                    except Exception as e:
                        st.error(f"❌ Erreur lors de l'analyse: {str(e)}")
                        db.rollback()

# ===== FIL DE DISCUSSION =====
elif menu == "🧵 Fil de discussion":
    st.header("🧵 Historique des interactions")
    
    contacts = db.query(Contact).all()
    
    if not contacts:
        st.warning("⚠️ Aucun contact disponible.")
    else:
        contact = st.selectbox(
            "Choisir un contact",
            contacts,
            format_func=lambda c: f"{c.name} ({c.domain or 'Sans domaine'})"
        )
        
        interactions = db.query(Interaction).filter(
            Interaction.contact_id == contact.id
        ).order_by(Interaction.date.desc()).all()
        
        st.divider()
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.metric("Nombre d'interactions", len(interactions))
        
        with col2:
            synthesize_btn = st.button("🧠 Générer synthèse IA", use_container_width=True)
        
        if synthesize_btn and interactions:
            with st.spinner("🤖 Génération de la synthèse..."):
                try:
                    synthesis = synthesize_thread(interactions)
                    st.markdown("### 📋 Synthèse globale du fil")
                    st.success(synthesis)
                except Exception as e:
                    st.error(f"❌ Erreur: {str(e)}")
        
        st.divider()
        
        if not interactions:
            st.info("ℹ️ Aucune interaction enregistrée pour ce contact")
        else:
            for idx, i in enumerate(interactions, 1):
                with st.expander(f"📅 {i.date.strftime('%d/%m/%Y %H:%M')} - Interaction #{len(interactions) - idx + 1}"):
                    st.markdown(f"**Importance:** {i.importance}")
                    st.markdown(f"**Utile:** {'✅ Oui' if i.useful else '❌ Non'}")
                    st.markdown("**Points discutés:**")
                    st.write(i.key_points)
                    if i.next_action:
                        st.markdown("**Action suivante:**")
                        st.write(i.next_action)

# ===== SIGNATURE CONTACT =====
elif menu == "✍️ Signature Contact":
    st.header("✍️ Signer un contact")
    
    contacts = db.query(Contact).filter(Contact.signed == False).all()
    
    if not contacts:
        st.info("ℹ️ Aucun contact en attente de signature")
    else:
        contact = st.selectbox(
            "Contact à signer",
            contacts,
            format_func=lambda c: f"{c.name} ({c.domain or 'Sans domaine'})"
        )
        
        st.write(f"**Email:** {contact.email or 'Non renseigné'}")
        st.write(f"**Téléphone:** {contact.phone or 'Non renseigné'}")
        
        st.divider()
        
        note = st.text_area(
            "Note / Accord signé",
            placeholder="Détails de l'accord, montant, durée, etc.",
            height=150
        )
        
        if st.button("✍️ Signer le contact", use_container_width=True):
            try:
                contact.signed = True
                contact.signed_at = datetime.utcnow()
                contact.signature_note = note
                db.commit()
                
                st.success(f"✅ Contact '{contact.name}' signé avec succès!")
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Erreur: {str(e)}")
                db.rollback()

# ===== TABLEAU DE BORD =====
elif menu == "📊 Tableau de bord":
    st.header("📊 Vue d'ensemble")
    
    total_contacts = db.query(Contact).count()
    signed_contacts = db.query(Contact).filter(Contact.signed == True).count()
    total_interactions = db.query(Interaction).count()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("👥 Contacts totaux", total_contacts)
    
    with col2:
        st.metric("✍️ Contacts signés", signed_contacts)
    
    with col3:
        st.metric("💬 Interactions", total_interactions)
    
    st.divider()
    
    st.subheader("📋 Derniers contacts ajoutés")
    recent_contacts = db.query(Contact).order_by(Contact.id.desc()).limit(5).all()
    
    if recent_contacts:
        for c in recent_contacts:
            with st.container():
                col1, col2, col3 = st.columns([2, 2, 1])
                with col1:
                    st.write(f"**{c.name}**")
                with col2:
                    st.write(f"{c.domain or 'Sans domaine'}")
                with col3:
                    st.write("✅" if c.signed else "⏳")
                st.divider()
    else:
        st.info("ℹ️ Aucun contact enregistré")

# Footer
st.sidebar.divider()
st.sidebar.caption("networkIN v1.0 - Propulsé par l'IA")
