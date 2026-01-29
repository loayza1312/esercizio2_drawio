def skill_extractor(text):
    # Qui andrebbe la chiamata a Gemini/GPT-4
    # Per ora simuliamo un'estrazione strutturata (JSON)
    if "HPLC" in text:
        return ["Analisi Chimica", "HPLC", "Controllo Qualità"]
    if "Python" in text:
        return ["Data Science", "Python", "AI"]
    if "Normative" in text:
        return ["Regulatory", "Compliance", "EMA"]
    return ["Competenze Generiche"]

def rag_search(query, mock_database):
    # Simula il RAG Engine che cerca nel Vector Database
    results = []
    for entry in mock_database:
        if query.lower() in str(entry['skills']).lower():
            results.append(entry)
    return results