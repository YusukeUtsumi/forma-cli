import os

from generator.sqlalchemy_generator import generate_model
from generator.api_generator import generate_router
from generator.main_generator import generate_main
from generator.database_generator import generate_database
from generator.er_generator import save_er


def generate_project(domain):

    os.makedirs("generated_app", exist_ok=True)

    os.makedirs("generated_app/models", exist_ok=True)
    os.makedirs("generated_app/routers", exist_ok=True)

    # models & routers
    for entity in domain.entities.values():

        model_code = generate_model(entity)

        with open(
            f"generated_app/models/{entity.name.lower()}.py", "w"
        ) as f:
            f.write(model_code)

        router_code = generate_router(entity)

        with open(
            f"generated_app/routers/{entity.name.lower()}s.py", "w"
        ) as f:
            f.write(router_code)

    # main.py
    main_code = generate_main(domain)

    with open("generated_app/main.py", "w") as f:
        f.write(main_code)

    # database.py
    db_code = generate_database()

    with open("generated_app/database.py", "w") as f:
        f.write(db_code)

    # ER diagram
    save_er(domain)