def generate_model(entity):

    fields = ""

    for f in entity.fields:
        fields += f"    {f} = Column(String)\n"

    return f"""
from sqlalchemy import Column, Integer, String
from database import Base

class {entity.name}(Base):

    __tablename__ = "{entity.name.lower()}"

    id = Column(Integer, primary_key=True)

{fields}
"""