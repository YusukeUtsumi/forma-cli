import re

def extract_relations(text):

    relations = []

    sentences = re.split(r"[.\n]", text)

    for s in sentences:

        s = s.lower()

        if "customer" in s and "order" in s:
            relations.append(("Customer", "Order"))

        if "order" in s and "product" in s:
            relations.append(("Order", "Product"))

    return relations