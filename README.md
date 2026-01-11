network/
│
├── app.py                    # Point d'entrée Streamlit
├── requirements.txt          # Librairies Python
├── network_config.py         # Configuration de l'application
├── db/
│   ├── __init__.py
│   ├── database.py           # Gestion SQLite locale
│   ├── models.py             # Modèles SQLAlchemy
│   └── crud.py               # Fonctions CRUD pour gérer les contacts
│
├── ai/
│   ├── __init__.py
│   ├── nlp_analysis.py       # Analyse des conversations avec IA
│   └── summarizer.py         # Génération points clés / stratégie
│
├── utils/
│   ├── __init__.py
│   ├── notifications.py      # Notifications locales
│   └── security.py           # Chiffrement local pour protection des données
│
└── README.md