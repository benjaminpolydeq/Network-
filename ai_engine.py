import openai

openai.api_key = "TON_CLE_OPENAI"

def analyse_discussion(text):
    """Analyse texte et renvoie résumé + score d'importance + suggestions """
    prompt = f"""
    Résume les points clés de cette interaction et propose des prochaines actions.
    Classe aussi l’échange par importance (Low/Medium/High).

    Texte:
    {text}
    """
    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )
    data = res.choices[0].message.content.strip().split("\n")
    return {
        "summary": data[0],
        "next_actions": data[1:-1],
        "importance": data[-1]
    }