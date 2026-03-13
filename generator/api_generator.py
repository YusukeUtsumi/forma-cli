def generate_router(entity):

    name = entity.name.lower()

    return f"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}s")
def list_{name}s():
    return []

@router.post("/{name}s")
def create_{name}(item: dict):
    return item
"""