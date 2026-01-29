import streamlit as st
import os
import requests
from modules.pdf_engine import extract_text_from_pdf
from modules.ai_logic import skill_extractor, rag_search

st.set_page_config(page_title="Local HR AI", layout="wide")

# Controllo Stato Modello Locale
st.sidebar.title("🤖 Local AI Status")
try:
    requests.get("http://localhost:11434/api/tags")
    st.sidebar.success("Ollama: ONLINE")
    st.sidebar.info("Modello: Phi-3 (Local)")
except:
    st.sidebar.error("Ollama: OFFLINE")
    st.sidebar.warning("Esegui 'ollama serve' nel terminale")

st.title("🏢 Valorizzazione Capitale Umano (Modello Locale)")

# --- Ingestion ---
st.header("1. Estrazione Competenze Locale")
if st.button("🔄 Analizza CV con IA Locale"):
    if not os.path.exists('cv_database'):
        st.error("Cartella cv_database non trovata!")
    else:
        files = [f for f in os.listdir('cv_database') if f.endswith('.pdf')]
        st.session_state.db_profili = []
        
        progress_bar = st.progress(0)
        for i, f in enumerate(files):
            path = os.path.join('cv_database', f)
            raw_text = extract_text_from_pdf(path)
            # Chiamata al modello locale
            with st.spinner(f"L'IA sta leggendo {f}..."):
                skills = skill_extractor(raw_text)
            
            st.session_state.db_profili.append({
                "nome": f,
                "skills": skills,
                "text": raw_text
            })
            progress_bar.progress((i + 1) / len(files))
        st.success("Analisi completata localmente!")

# --- Search ---
st.header("2. Ricerca Intelligente")
query = st.text_input("Cosa cerchi? (Es: Esperto di reattori chimici)")
if query and 'db_profili' in st.session_state:
    with st.spinner("Ricerca nel database locale..."):
        risultati = rag_search(query, st.session_state.db_profili)
    
    if risultati:
        for r in risultati:
            with st.expander(f"👤 {r['nome']}"):
                st.write(f"**Skills:** {', '.join(r['skills'])}")
    else:
        st.warning("Nessun match trovato.")