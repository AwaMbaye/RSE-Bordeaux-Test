print("""
🌍 OBJECTIFS DE DÉVELOPPEMENT DURABLE (ODD) :

Les Objectifs de Développement Durable (ODD) sont un appel universel à l'action pour éliminer la pauvreté, protéger la planète et garantir la prospérité pour tous, dans le cadre d'un nouvel agenda de développement durable. Adoptés par tous les États membres de l'ONU en 2015, les ODD fournissent un plan mondial pour parvenir à un avenir meilleur pour tous, d'ici à 2030.

COMMENT CLASSIFIER LES ACTIONS RSE SELON LES ODD ?

Pour classer les actions RSE en fonction des Objectifs de Développement Durable, nous utilisons une approche basée sur l'identification de mots-clés associés à chaque ODD. Chaque action RSE est analysée et attribuée à la catégorie correspondant à l'ODD auquel elle contribue le plus directement.

Les 17 Objectifs de Développement Durable sont les suivants :
🛑 Pas de pauvreté
🍽️ Faim zéro
💊 Bonne santé et bien-être
📚 Éducation de qualité
⚖️ Égalité entre les sexes
🚿 Eau propre et assainissement
⚡ Énergie propre et d'un coût abordable
💼 Travail décent et croissance économique
🏗️ Industrie, innovation et infrastructure
🤝 Inégalités réduites
🏙️ Villes et communautés durables
🌱 Consommation et production responsables
🌍 Mesures relatives à la lutte contre les changements climatiques
🐟 Vie aquatique
🌳 Vie terrestre
☮️ Paix, justice et institutions efficaces
🤝 Partenariats pour la réalisation des objectifs
""")

from data_manager import get_data

def classify_actions_rse_ODD(data):
    data, _ = get_data() 
    
    criteria = {
        "Pas de pauvreté": [],
        "Faim zéro": [],
        "Bonne santé et bien-être": [],
        "Éducation de qualité": [],
        "Égalité entre les sexes": [],
        "Eau propre et assainissement": [],
        "Énergie propre et d'un coût abordable": [],
        "Travail décent et croissance économique": [],
        "Industrie, innovation et infrastructure": [],
        "Inégalités réduites": [],
        "Villes et communautés durables": [],
        "Consommation et production responsables": [],
        "Mesures relatives à la lutte contre les changements climatiques": [],
        "Vie aquatique": [],
        "Vie terrestre": [],
        "Paix, justice et institutions efficaces": [],
        "Partenariats pour la réalisation des objectifs": [],
        "Autres": []
    }

    keywords = {
        "Pas de pauvreté": ["pauvreté", "précarité", "exclusion sociale", "accès aux ressources", "sécurité alimentaire"],
        "Faim zéro": ["faim", "malnutrition", "sécurité alimentaire", "agriculture durable"],
        "Bonne santé et bien-être": ["santé", "bien-être", "accès aux soins", "prévention des maladies"],
        "Éducation de qualité": ["éducation", "alphabétisation", "accès à l'éducation", "formation professionnelle"],
        "Égalité entre les sexes": ["égalité des genres", "droits des femmes", "participation des femmes"],
        "Eau propre et assainissement": ["eau potable", "assainissement", "gestion de l'eau"],
        "Énergie propre et d'un coût abordable": ["énergie propre", "énergies renouvelables", "accès à l'énergie"],
        "Travail décent et croissance économique": ["travail décent", "emploi", "croissance économique"],
        "Industrie, innovation et infrastructure": ["industrie", "innovation", "infrastructures"],
        "Inégalités réduites": ["inégalités", "répartition des richesses", "justice sociale"],
        "Villes et communautés durables": ["villes durables", "communautés durables", "urbanisation"],
        "Consommation et production responsables": ["consommation responsable", "production responsable", "gestion des déchets"],
        "Mesures relatives à la lutte contre les changements climatiques": ["changement climatique", "atténuation", "adaptation"],
        "Vie aquatique": ["océans", "ressources marines", "conservation marine"],
        "Vie terrestre": ["biodiversité", "conservation des écosystèmes", "déforestation"],
        "Paix, justice et institutions efficaces": ["paix", "justice", "institutions"],
        "Partenariats pour la réalisation des objectifs": ["partenariats", "coopération internationale", "engagement"],
    }

    for record in data:
        action_rse = record.get("action_rse", "").lower()
        company_info = {
            "name": record.get("nom_courant_denomination", "N/A"),
            "action_rse": action_rse,
            "activity": record.get("libelle_section_naf", "N/A"),
            "city": record.get("commune", "N/A")
        }
        found_category = False
        for criterion, key_phrases in keywords.items():
            if any(key_phrase in action_rse for key_phrase in key_phrases):
                criteria[criterion].append(company_info)
                found_category = True
                break  
        
     
        if not found_category:
            criteria["Autres"].append(company_info)

    return criteria