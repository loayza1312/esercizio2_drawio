from fpdf import FPDF
import os

class CV(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Curriculum Vitae - Profilo Professionale', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf(filename, data):
    pdf = CV()
    pdf.add_page()
    
    pdf.chapter_title("Dati Anagrafici")
    pdf.chapter_body(f"Nome: {data['nome']}\nSede: {data['sede']}\nRuolo: {data['ruolo']}")
    
    pdf.chapter_title("Competenze Tecniche")
    pdf.chapter_body(data['competenze'])
    
    pdf.chapter_title("Ultimi Progetti e Certificazioni")
    pdf.chapter_body(data['progetti'])
    
    pdf.output(filename)

# Dati per i 5 CV (Esercizio 2 - Azienda Chimico-Farmaceutica)
profili = [
    {
        "nome": "Marco Bianchi",
        "sede": "Milano, Italia",
        "ruolo": "Ricercatore Senior in Chimica Organica",
        "competenze": "Sintesi polimerica, Spettroscopia NMR, Cromatografia (HPLC).",
        "progetti": "Risoluzione problema di stabilità nel composto X22. Certificazione Green Chemistry 2023."
    },
    {
        "nome": "Chen Wei",
        "sede": "Singapore",
        "ruolo": "Data Scientist Farmaceutico",
        "competenze": "Machine Learning applicato al drug discovery, Python, R, Analisi predittiva.",
        "progetti": "Sviluppo algoritmo per screening molecolare rapido. Corso avanzato AI in Healthcare."
    },
    {
        "nome": "Elena Rossi",
        "sede": "Milano, Italia",
        "ruolo": "Specialista Affari Regolatori",
        "competenze": "Normative EMA, FDA, Documentazione tecnica per brevetti.",
        "progetti": "Approvazione rapida farmaco antinfiammatorio. Master in Diritto Farmaceutico internazionale."
    },
    {
        "nome": "John Smith",
        "sede": "Boston, USA",
        "ruolo": "Ingegnere di Processo",
        "competenze": "Scale-up industriale, Ottimizzazione reattori chimici, Six Sigma.",
        "progetti": "Riduzione costi produzione del 15% nel sito di Boston. Certificazione Black Belt Lean."
    },
    {
        "nome": "Aiko Tanaka",
        "sede": "Tokyo, Giappone",
        "ruolo": "Biochimica",
        "competenze": "Ingegneria enzimatica, CRISPR, Fermentazione controllata.",
        "progetti": "Nuovo metodo di estrazione proteica. Pubblicazione su Nature sul microbioma sintetico."
    }
]

# Creazione cartella per i CV
if not os.path.exists('cv_database'):
    os.makedirs('cv_database')

for i, profilo in enumerate(profili):
    nome_file = f"cv_database/cv_{i+1}.pdf"
    create_pdf(nome_file, profilo)
    print(f"Creato: {nome_file}")