import re

def extract_fields(text):

    fields = {}

    sentences = re.split(r"[.\n]", text)

    for s in sentences:

        s = s.lower()

        if "customer" in s and "have" in s:

            fields.setdefault("Customer", [])

            if "name" in s:
                fields["Customer"].append("name")

            if "email" in s:
                fields["Customer"].append("email")

    return fields