import re

def extract_entities(text):

    entities = set()

    words = re.findall(r"[A-Za-z]+", text)

    for w in words:

        w = w.lower()

        if w in ["customer", "customers"]:
            entities.add("Customer")

        if w in ["order", "orders"]:
            entities.add("Order")

        if w in ["product", "products"]:
            entities.add("Product")

    return list(entities)