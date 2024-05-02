import PyPDF2
import spacy
from impactscoreTest import classify_actions_rse_impact_score
from ODD import classify_actions_rse_ODD

# Chargement du modèle spaCy
nlp = spacy.load("fr_core_news_sm")

# Étape 1 : Prétraitement des documents PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Étape 2 : Traitement du langage naturel (NLP)
def process_text(text):
    doc = nlp(text)
    return doc

# Étape 3 : Extraction d'informations clés
def extract_key_information(doc):
    key_information = []
    for entity in doc.ents:
        if entity.label_ == "ORG":  
            name = entity.text
            if name[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:  
                key_information.append(f"l'{name}")
            else:
                key_information.append(f"le {name}")
    return key_information

# Étape 4 : Modélisation
def generate_transition_plan(key_information, impact_score_criteria, odd_criteria):
    transition_plan = "Voici votre plan de transition : \n\n"
    
    transition_plan += "Informations clés :\n"
    for info in key_information:
        transition_plan += f"- {info}\n"
    
    transition_plan += "\nCritères d'impact score :\n"
    for criterion, companies in impact_score_criteria.items():
        transition_plan += f"- {criterion}:\n"
        for company in companies:
            transition_plan += f"  * {company['name']} ({company['activity']}, {company['city']})\n"

    transition_plan += "\nCritères ODD :\n"
    for criterion, companies in odd_criteria.items():
        transition_plan += f"- {criterion}:\n"
        for company in companies:
            transition_plan += f"  * {company['name']} ({company['activity']}, {company['city']})\n"
    
    return transition_plan


# Étape 5 : Intégration avec le RAG de Hugging Face
def generate_plan_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    doc = process_text(text)
    key_information = extract_key_information(doc)
    impact_score_criteria = classify_actions_rse_impact_score(doc)
    odd_criteria = classify_actions_rse_ODD(doc)  # Utiliser la fonction ODD
    transition_plan = generate_transition_plan(key_information, impact_score_criteria, odd_criteria)
    return transition_plan

# Étape 6 : Test et validation
pdf_path = "trans1.pdf"
transition_plan = generate_plan_from_pdf(pdf_path)
print(transition_plan)
