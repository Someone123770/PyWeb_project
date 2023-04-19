import datetime

import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    reg_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    role = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    user_role = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    github_ref = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telegram_ref = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    platform = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_settings = orm.relationship("Users_settings", back_populates='user')
    user_projects = orm.relationship("Users_projects", back_populates='user')
    activity = orm.relationship('Change_log', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
