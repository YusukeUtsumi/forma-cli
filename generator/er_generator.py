def generate_er(domain):

    lines = ["erDiagram"]

    for r in domain.relations:
        lines.append(f"{r.source} ||--o{{ {r.target}")

    return "\n".join(lines)


def save_er(domain, output_path="generated_app/schema.er"):

    er_code = generate_er(domain)

    with open(output_path, "w") as f:
        f.write(er_code)