import sys

from parser.entity_extractor import extract_entities
from parser.relation_extractor import extract_relations
from parser.field_extractor import extract_fields

from domain.domain_model import DomainModel

from generator.er_generator import generate_er
from generator.project_generator import generate_project


def run(text):

    entities = extract_entities(text)
    relations = extract_relations(text)
    fields = extract_fields(text)

    domain = DomainModel()

    for e in entities:
        domain.add_entity(e)

    for entity, fs in fields.items():
        for f in fs:
            domain.add_field(entity, f)

    for a, b in relations:
        domain.add_relation(a, b)

    er = generate_er(domain)

    print("\nER Diagram\n")
    print(er)

    generate_project(domain)

    print("\nProject generated in generated_app\n")


if __name__ == "__main__":

    cmd = sys.argv[1]
    text = sys.argv[2]

    if cmd == "dev":
        run(text)