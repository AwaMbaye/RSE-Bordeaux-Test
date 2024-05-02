print("""
🌍 QU'EST-CE QUE LA NORME ISO 26000 ?

La norme ISO 26000 propose une grille de lecture de la thématique développement durable ultra-pratique pour déployer une politique RSE d'entreprise bien structurée, qui ne laisse rien de côté. Publiée en 2010, cette norme volontaire a été élaborée en concertation avec près de 90 pays à travers le monde, dont la France.

COMMENT EST-ELLE STRUCTURÉE ?

ISO 26000 : Une grille de lecture à 7 entrées

🏢 La gouvernance de la structure
👨‍👩‍👧‍👦 Les droits humains
🤝 Les conditions et relations de travail
🌱 La responsabilité environnementale
⚖️ La loyauté des pratiques
🛍️ Les questions relatives au consommateur et à la protection du consommateur
🌍 Les communautés et le développement local.
Source AFNOR : www.afnor.org/developpement-durable/demarche-iso-26000/
""")

from data_manager import get_data

def classify_actions_rse_impact_score(data):
    data, _ = get_data() 
    
    criteria = {
        "Innovation sociale et économique": [],
        "Diversité et inclusion": [],
        "Engagement communautaire ": [],
        "Autres": []
    }

    keywords = {
    "Innovation sociale et économique": ["partenariats sociaux", "bénéfices sociaux", "nouveaux produits sociaux"],
    "Diversité et inclusion": ["diversité en haut", "taux de rétention", "initiatives de diversité"],
    "Engagement communautaire": ["heures de bénévolat", "dons aux organisations locales", "taux de participation"]
    }

    for record in data:
        action_rse = record.get("action_rse", "").lower()
        impact_score = record.get("impact_score", "").lower()
        company_info = {
            "name": record.get("nom_courant_denomination", "N/A"),
            "action_rse": action_rse,
            "activity": record.get("libelle_section_naf", "N/A"),
            "city": record.get("commune", "N/A")
        }
        found_category = False
        for criterion, key_phrases in keywords.items():
            if any(key_phrase in impact_score for key_phrase in key_phrases):
                criteria[criterion].append(company_info)
                found_category = True
                break 
        

        if not found_category:
            criteria["Autres"].append(company_info)

    return criteria