from owlready2 import *
from difflib import get_close_matches

onto = get_ontology("FombaGasy.rdf").load()

# Optionnel (HermiT nécessite Java) : commente si tu n'en as pas besoin
def try_reasoners():
    # HermiT
    try:
        with onto:
            sync_reasoner()   # HermiT
        print("HermiT OK")
        return "HermiT"
    except Exception as e:
        print("HermiT error:", e)

    # Pellet
    try:
        with onto:
            sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)
        print("Pellet OK")
        return "Pellet"
    except Exception as e:
        print("⚠️ Pellet error:", e)

    print("Aucun reasoner n'a pu s'exécuter, on continue sans inférences.")
    return "None"

print("Ontologie chargée")

def get_label_or_name(x):
    # label prioritaire
    if hasattr(x, "label") and x.label:
        return str(x.label[0])
    # sinon name
    if hasattr(x, "name"):
        return x.name
    return str(x)

def all_terms_index():
    """Index de recherche : (type, objet, textes)"""
    idx = []
    for c in onto.classes():
        texts = [c.name.lower()]
        if hasattr(c, "label"):
            texts += [str(l).lower() for l in (c.label or [])]
        idx.append(("class", c, texts))
    for i in onto.individuals():
        texts = [i.name.lower()]
        if hasattr(i, "label"):
            texts += [str(l).lower() for l in (i.label or [])]
        idx.append(("ind", i, texts))
    return idx

INDEX = all_terms_index()

def find_entities(term, limit=10):
    """Trouve classes/individus correspondant au terme (partiel + labels)."""
    t = term.lower()
    hits = []
    for kind, obj, texts in INDEX:
        if any(t in txt for txt in texts):
            hits.append((kind, obj))
    return hits[:limit]

def neighbors_of_individual(ind, limit=30):
    """Suggestions basées sur les relations de l'individu (sortants + entrants)."""
    s = set()

    # sortants: ind --prop--> val
    for prop in ind.get_properties():
        for val in prop[ind]:
            s.add(get_label_or_name(val))

    # entrants: other --prop--> ind
    for other in onto.individuals():
        for prop in other.get_properties():
            if ind in prop[other]:
                s.add(get_label_or_name(other))

    return sorted(s)[:limit]

def instances_of_class(cls, limit=30):
    return sorted({get_label_or_name(i) for i in cls.instances()})[:limit]

def did_you_mean(term, limit=8):
    """Suggestions de correction (proches) si aucun match direct."""
    candidates = []
    for kind, obj, texts in INDEX:
        candidates.extend(texts)  # names + labels
    # dédoublonner
    candidates = sorted(set(candidates))
    return get_close_matches(term.lower(), candidates, n=limit, cutoff=0.6)

def suggest(term):
    hits = find_entities(term, limit=10)

    # Si on a trouvé des entités, on renvoie des suggestions "liées"
    if hits:
        results = []
        for kind, obj in hits:
            title = f"{'Classe' if kind=='class' else 'Individu'}: {get_label_or_name(obj)}"
            if kind == "class":
                sugg = instances_of_class(obj)
            else:
                sugg = neighbors_of_individual(obj)
            results.append((title, sugg))
        return {"matches": results, "did_you_mean": []}

    # Sinon on propose des mots proches
    return {"matches": [], "did_you_mean": did_you_mean(term)}

print("\nClasses :")
for classes in onto.classes():
    print("-", classes.name, list(classes.label))
    
print("\nIndividus :")
for individus in onto.individuals():
    print("-", individus.name, list(individus.label))
    
print("\nTypes des individus :")
for ind in onto.individuals():
    print(f"- {ind.name} est un(e) :")
    for classe in ind.is_a:
        print("   →", classe.name)
        
# Boucle de test
while True:
    user_input = input("\nEntrez un mot (ou 'exit' pour quitter) : ").strip()
    if user_input.lower() == "exit":
        print("Veloma e !")
        break

    out = suggest(user_input)

    if out["matches"]:
        for title, sugg in out["matches"]:
            print(f"\n{title}")
            if sugg:
                print("  → Suggestions:", sugg)
            else:
                print("  → (Aucune relation/instance trouvée)")
    else:
        if out["did_you_mean"]:
            print(f"Aucun match exact. Tadiavinao ve ny hoe: {out['did_you_mean']} ?")
        else:
            print(f"Aucune suggestion trouvée pour '{user_input}'")