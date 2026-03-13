class Entity:

    def __init__(self, name):
        self.name = name
        self.fields = []


class Relation:

    def __init__(self, source, target, cardinality="1:N"):
        self.source = source
        self.target = target
        self.cardinality = cardinality


class DomainModel:

    def __init__(self):
        self.entities = {}
        self.relations = []

    def add_entity(self, name):
        if name not in self.entities:
            self.entities[name] = Entity(name)

    def add_field(self, entity, field):
        if entity in self.entities:
            self.entities[entity].fields.append(field)

    def add_relation(self, source, target):
        self.relations.append(Relation(source, target))