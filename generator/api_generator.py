def generate_router(entity):

    name = entity.name.lower()
    cname = entity.name

    return f"""
from fastapi import APIRouter
from database import SessionLocal
from models.{name} import {cname}

router = APIRouter()


@router.get("/{name}s")
def list_{name}s():

    db = SessionLocal()

    items = db.query({cname}).all()

    return items


@router.post("/{name}s")
def create_{name}(item: dict):

    db = SessionLocal()

    obj = {cname}(**item)

    db.add(obj)

    db.commit()

    db.refresh(obj)

    return obj
"""