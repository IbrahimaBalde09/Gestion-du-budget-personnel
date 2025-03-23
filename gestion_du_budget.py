import json

def charger_budget():
    """Charge le budget à partir d'un fichier JSON ou crée un nouveau budget."""
    try:
        with open("budget.json", "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return {"revenus": [], "dépenses": []}

def sauvegarder_budget(budget):
    """Sauvegarde le budget dans un fichier JSON."""
    with open("budget.json", "w", encoding="utf-8") as fichier:
        json.dump(budget, fichier, indent=4)

def ajouter_revenu(budget):
    """Ajoute un revenu au budget."""
    source = input("Source du revenu : ")
    montant = float(input("Montant : "))
    budget["revenus"].append({"source": source, "montant": montant})
    sauvegarder_budget(budget)
    print("Revenu ajouté avec succès !")

def ajouter_depense(budget):
    """Ajoute une dépense au budget."""
    categorie = input("Catégorie de dépense : ")
    montant = float(input("Montant : "))
    budget["dépenses"].append({"catégorie": categorie, "montant": montant})
    sauvegarder_budget(budget)
    print("Dépense ajoutée avec succès !")

def afficher_budget(budget):
    """Affiche un résumé du budget."""
    total_revenus = sum(item["montant"] for item in budget["revenus"])
    total_depenses = sum(item["montant"] for item in budget["dépenses"])
    solde = total_revenus - total_depenses

    print("\n--- RÉSUMÉ DU BUDGET ---")
    print(f"Total des revenus : {total_revenus:.2f}€")
    print(f"Total des dépenses : {total_depenses:.2f}€")
    print(f"Solde restant : {solde:.2f}€")

def menu():
    """Affiche le menu principal et gère les interactions utilisateur."""
    budget = charger_budget()
    while True:
        print("\n1. Ajouter un revenu")
        print("2. Ajouter une dépense")
        print("3. Afficher le budget")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_revenu(budget)
        elif choix == "2":
            ajouter_depense(budget)
        elif choix == "3":
            afficher_budget(budget)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()