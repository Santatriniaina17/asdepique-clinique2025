from owlready2 import *
from difflib import get_close_matches
import os

# ========================
# Chargement ontologie
# ========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ONTO_PATH = os.path.join(BASE_DIR, "data", "ontology.rdf")

onto = get_ontology(ONTO_PATH).load()


# ========================
# Utils robustes
# ========================

def get_label_or_name(x):
    """
    Gère entités OWL + littéraux (locstr)
    """
    if isinstance(x, (str, locstr)):
        return str(x)

    if hasattr(x, "label") and x.label:
        return str(x.label[0])

    if hasattr(x, "name"):
        return x.name

    return str(x)


# ========================
# Index de recherche
# ========================

def build_index():
    idx = []

    for c in onto.classes():
        texts = [c.name.lower()]
        texts += [str(l).lower() for l in (c.label or [])]
        idx.append(("class", c, texts))

    for i in onto.individuals():
        texts = [i.name.lower()]
        texts += [str(l).lower() for l in (i.label or [])]
        idx.append(("individual", i, texts))

    return idx


INDEX = build_index()


# ========================
# Logique sémantique
# ========================

def instances_of_class(cls, limit=20):
    return [get_label_or_name(i) for i in cls.instances()][:limit]


def neighbors_of_individual(ind, limit=20):
    """
    Ne retourne QUE des entités OWL (pas de littéraux)
    """
    s = set()

    # sortants
    for prop in ind.get_properties():
        for val in prop[ind]:
            if hasattr(val, "name"):
                s.add(get_label_or_name(val))

    # entrants
    for other in onto.individuals():
        for prop in other.get_properties():
            if ind in prop[other]:
                s.add(get_label_or_name(other))

    return sorted(s)[:limit]


def did_you_mean(term, limit=8):
    candidates = []
    for _, _, texts in INDEX:
        candidates.extend(texts)

    candidates = sorted(set(candidates))
    return get_close_matches(term.lower(), candidates, n=limit, cutoff=0.6)


def suggest(term):
    t = term.lower()
    matches = []

    for kind, obj, texts in INDEX:
        if any(t in txt for txt in texts):

            if kind == "class":
                matches.append({
                    "type": "class",
                    "label": get_label_or_name(obj),
                    "suggestions": instances_of_class(obj)
                })

            else:  # individual
                matches.append({
                    "type": "individual",
                    "label": get_label_or_name(obj),
                    "suggestions": neighbors_of_individual(obj)
                })

    if matches:
        return {
            "matches": matches,
            "did_you_mean": []
        }

    return {
        "matches": [],
        "did_you_mean": did_you_mean(term)
    }
