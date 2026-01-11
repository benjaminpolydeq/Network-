import openai

openai.api_key = "YOUR_OPENAI_KEY"

def analyze_conversation(text: str):
    """
    Analyse une conversation et renvoie:
    - points clés
    - stratégie
    - degré d'utilité
    """
    prompt = f"""
    Analyse cette conversation : {text}
    1. Résume les points clés
    2. Propose une stratégie de coopération
    3. Évalue si la discussion est utile, crédible et fructueuse (échelle 1-5)
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response['choices'][0]['message']['content']