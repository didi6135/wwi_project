from app.db.database import session_maker
from app.db.modeles.country import Country


def get_all_countries():
    with session_maker() as session:
        return session.query(Country).all()


def get_country_by_id(country_id):
    with session_maker() as session:
        return session.query(Country).filter_by(country_id=country_id).first()