import requests
import json

def call_local_model(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "phi3:mini",
        "prompt": prompt,
        "stream": False,
        "format": "json" # Chiediamo un output strutturato
    }
    
    try:
        response = requests.post(url, json=data)
        return json.loads(response.text)['response']
    except Exception as e:
        return f"Errore connessione Ollama: {e}"

def skill_extractor(text):
    prompt = f"""
    Analizza il seguente CV e restituisci un oggetto JSON con una lista di 'skills'.
    Estrai solo le competenze tecniche principali.
    Testo del CV: {text}
    Rispondi solo in formato JSON: {{"skills": ["skill1", "skill2"]}}
    """
    response = call_local_model(prompt)
    try:
        return json.loads(response)['skills']
    except:
        return ["Errore estrazione"]

def rag_search(query, mock_database):
    # Usiamo il modello locale per decidere se c'è un match
    results = []
    for entry in mock_database:
        prompt = f"La competenza '{query}' è correlata a queste competenze: {entry['skills']}? Rispondi solo 'SI' o 'NO'."
        match = call_local_model(prompt)
        if "SI" in match.upper():
            results.append(entry)
    return results