📒 AI-Powered Personal Networking Agenda
Private • Intelligent • On-Device
Une application intelligente de type agenda / personal CRM, conçue pour aider les utilisateurs à suivre, analyser et valoriser leurs interactions de networking, tout en garantissant une confidentialité totale des données (local-only).
🚀 Présentation
AI-Powered Personal Networking Agenda est une application qui permet aux utilisateurs de :
Enregistrer les personnes rencontrées (networking)
Documenter les discussions et interactions
Analyser automatiquement les échanges grâce à l’IA
Générer des résumés, stratégies et prochaines actions
Planifier des rendez-vous et rappels intelligents
Travailler hors ligne, sans fuite de données
👉 Toutes les données restent sur l’appareil de l’utilisateur.
🎯 Problème résolu
La majorité des outils CRM sont :
Complexes
Orientés entreprises
Centralisés sur le cloud
Peu respectueux de la confidentialité
Cette application propose une alternative : ✅ personnelle
✅ simple
✅ intelligente
✅ sécurisée
🧠 Fonctionnalités clés
📇 Gestion des contacts
Nom
Email / Téléphone
Domaine d’activité
Contexte de rencontre (événement, réunion, etc.)
💬 Suivi des interactions
Notes textuelles
Historique des discussions
Date & contexte
Prochaine action à effectuer
🤖 Analyse IA des discussions
Résumé automatique des points clés
Extraction des sujets abordés
Proposition de stratégie de coopération
Évaluation de la discussion :
Utile / Non utile
Crédible / Non crédible
Fructueuse / À suivre
Classification par niveau d’importance
⏰ Agenda & rappels
Rendez-vous programmés
Notifications intelligentes
Suivi des prochaines actions
🔐 Sécurité & confidentialité
Stockage local (SQLite)
Aucun envoi de données vers des serveurs tiers
IA utilisable en local ou via API contrôlée
Idéal pour données sensibles
🏗️ Architecture technique
Copier le code

Frontend : Streamlit
Backend  : Python
Base de données : SQLite (local)
IA : OpenAI / LLM local (optionnel)
Stockage : 100% on-device
📁 Structure du projet
Copier le code

my_personal_crm/
├── app.py              # Interface Streamlit
├── ai_engine.py        # Analyse IA
├── db.py               # Base de données locale
├── requirements.txt
├── models/
│   ├── contact.py
│   └── interaction.py
└── utils.py
⚙️ Installation
1️⃣ Cloner le dépôt
Copier le code
Bash
git clone https://github.com/ton-username/my_personal_crm.git
cd my_personal_crm
2️⃣ Installer les dépendances
Copier le code
Bash
pip install -r requirements.txt
3️⃣ Lancer l’application
Copier le code
Bash
streamlit run app.py
🔑 Configuration IA
Dans ai_engine.py, configure ta clé API (ou un modèle local) :
Copier le code
Python
openai.api_key = "TA_CLE_API"
💡 Possibilité future :
LLM local (Ollama, LM Studio, ARSLM, etc.)
Mode 100% offline
📊 Cas d’usage
Entrepreneurs & freelances
Investisseurs
Étudiants & chercheurs
Leaders communautaires
Réseautage professionnel
Suivi de partenariats
🛣️ Roadmap
🔹 Phase 1 – MVP (actuelle)
Contacts & interactions
Analyse IA textuelle
Interface Streamlit
🔹 Phase 2
Enregistrement vocal + transcription
Notifications système
Intégration calendrier
🔹 Phase 3
Application mobile (Flutter / React Native)
Visualisation réseau (graph)
IA prédictive & scoring avancé
🧩 Améliorations futures envisagées
Chiffrement local AES
Synchronisation chiffrée multi-appareils
Mode entreprise / on-premise
Partage sécurisé entre utilisateurs
Plugin navigateur / mobile
📜 Licence
Propriétaire / Open-Core (au choix)
Usage personnel libre.
Usage commercial soumis à licence.
👤 Auteur
Benjamin Amaad Kama
Créateur & développeur
📧 flywithjesus@outlook.com