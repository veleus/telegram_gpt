
from model.database import User


def add_user(db, id_account, name):
    user = User(id_account=id_account, name = name)
    db.add(user)
    db.commit()
    db.refresh(user)

def get_user(db, id_account):
    return db.query(User).filter_by(id_account=id_account).first()

def get_all_users(db):
    return db.query(User.id, User.id_account, User.name, User.role).all()

def get_user_by_id(db, id_user):
    return db.query(User.name, User.role).filter_by(id_account=id_user).first()

def update_user(db, id_user):
    user = db.query(User).filter_by(id_account=id_user).first()
    user.role = 'role_admin'
    db.commit()
    db.refresh(user)


def get_user_by_id_admin(db, id_user):
    return db.query(User).filter_by(id_account=id_user).first()