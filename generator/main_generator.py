def generate_main(domain):

    imports = []
    includes = []

    for entity in domain.entities.values():

        name = entity.name.lower()

        imports.append(
            f"from routers.{name}s import router as {name}s_router"
        )

        includes.append(
            f"app.include_router({name}s_router)"
        )

    imports_code = "\n".join(imports)
    includes_code = "\n".join(includes)

    return f"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

{imports_code}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

{includes_code}
"""