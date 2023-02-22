# id
# team_leader (id) (id руководителя, целое число)
# job (description) (описание работы)
# work_size (hours) (объем работы в часах)
# collaborators (list of id of participants) (список id участников)
# start_date (дата начала)
# end_date (дата окончания)
# is_finished (bool) (признак завершения)
import datetime

import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    worksize = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    user = orm.relation('User')
