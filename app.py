import streamlit as st
import os
from modules.pdf_engine import extract_text_from_pdf
from modules.ai_logic import skill_extractor, rag_search

st.set_page_config(page_title="HR AI Intelligence", layout="wide")

# Sidebar - Memoria di Stato (come nel tuo diagramma)
st.sidebar.title("🧠 Stato Sistema")
st.sidebar.status("Database: Collegato")
st.sidebar.info("Modello AI: GPT-4o Mini\nStato: Pronto")

st.title("🏢 Valorizzazione Capitale Umano")
st.write("Sistema intelligente per mappare le competenze globali.")

# --- SEZIONE UPLOAD (Abbattimento barriera data-entry) ---
st.header("1. Ingestion Layer")
if st.button("🔄 Scansiona Cartella CV (cv_database)"):
    files = [f for f in os.listdir('cv_database') if f.endswith('.pdf')]
    
    # Simulazione Database Profili
    st.session_state.db_profili = []
    
    for f in files:
        path = os.path.join('cv_database', f)
        raw_text = extract_text_from_pdf(path)
        skills = skill_extractor(raw_text) # AI Skill Extractor
        
        st.session_state.db_profili.append({
            "nome": f,
            "skills": skills,
            "text": raw_text
        })
    st.success(f"Analizzati {len(files)} documenti. Competenze estratte e normalizzate nel Vector Database.")

# --- SEZIONE RAG & MATCHING (Eliminazione silos geografici) ---
st.header("2. Skill Matching & RAG Engine")
query = st.text_input("Di quale competenza hai bisogno oggi? (es. HPLC, Python...)")

if query and 'db_profili' in st.session_state:
    risultati = rag_search(query, st.session_state.db_profili)
    
    if risultati:
        st.subheader(f"Risultati per '{query}':")
        for r in risultati:
            with st.expander(f"👤 Candidato Interno: {r['nome']}"):
                st.write(f"**Competenze Rilevate:** {', '.join(r['skills'])}")
                st.write("**Analisi del CV:**")
                st.text(r['text'][:200] + "...")
    else:
        st.warning("Nessun profilo trovato internamente con questa competenza.")
elif query:
    st.error("Per favore, scansiona prima i documenti nel punto 1.")

# Footer grafico
st.markdown("---")
st.caption("Architettura Modulare v1.0 - Sviluppato su Codespaces")