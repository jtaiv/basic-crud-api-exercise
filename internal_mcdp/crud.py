from sqlalchemy.orm import Session

from . import models, schemas


def get_profile(db: Session, email: str):
    return db.query(models.Profile).filter(models.Profile.email == email).first()


def get_profile_by_name(db: Session, name: str):
    return db.query(models.Profile).filter(models.Profile.name == name).first()


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profile).offset(skip).limit(limit).all()


def create_profile(db: Session, profile: schemas.Profile):
    db_profile = models.Profile(email=profile.email, name=profile.name, contact=profile.contact)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_profile(db: Session, email: str):
    profile = db.query(models.Profile).filter(models.Profile.email == email).first()
    print(profile)
    db.delete(profile)
    db.commit()
