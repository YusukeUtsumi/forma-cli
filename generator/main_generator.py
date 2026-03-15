def generate_main(domain_model):

    router_imports = ""
    router_includes = ""

    for entity in domain_model.entities:

        name = entity.lower()

        router_imports += f"from routers import {name}s\n"
        router_includes += f"app.include_router({name}s.router)\n"

    return f"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from database import Base

from models import *

{router_imports}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# CREATE TABLES
# ------------------------

Base.metadata.create_all(bind=engine)

# ------------------------
# ROUTERS
# ------------------------

{router_includes}
"""