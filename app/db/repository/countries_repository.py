from app.db.database import session_maker
from app.db.modeles.country import Country


def get_all_countries():
    with session_maker() as session:
        return session.query(Country).all()
