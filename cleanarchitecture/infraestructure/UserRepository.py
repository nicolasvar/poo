from typing import List

import sqlalchemy
from domain.entity.DMLEntity import DMLEntity
from domain.entity.UserEntity import UserEntity
from domain.repository.IUserRepository import IUserRepository
from infraestructure.BaseRepository import BaseRepository

class UserRepository(BaseRepository, IUserRepository):
    items: List[UserEntity] =[]

    def findOne(self, id) -> UserEntity:
        db = sqlalchemy.create_engine(BaseRepository.conn)
        sql = sqlalchemy.text("SELECT * FROM Usuarios WHERE id = :id")
        with db.connect() as conn:
            dr = conn.execute(sql, {"id": id}).fetchone()
            if dr:
                return  UserEntity(id=dr[0], name=dr[1], email=dr[2], password=dr[3])
        return None
            
    def findAll(self)->List[UserEntity]:
        db = sqlalchemy.create_engine(BaseRepository.conn)
        sql = sqlalchemy.text("SELECT * FROM USUARIOS")
        items : List[UserEntity] = []
        with db.connect() as conn:
            dr = conn.execute(sql)
            for row in dr:
                items.append(UserEntity(id=row.id, name=row.name, email=row.email, password=row.password))
        return items
        
    def add(self,item)-> UserEntity:
        db = sqlalchemy.create_engine(BaseRepository.conn)
        sql = sqlalchemy.text(
            "INSERT INTO USUARIOS (name, email, password) VALUES(:name, :email, :password)")
        with db.connect() as conn:
            dr = conn.execute(
                sql, {"id":item.id, "name": item.name, "email": item.email, "password": item.password}
            )
            conn.commit()
        return DMLEntity()

    def update(self,item) ->UserEntity:
        db = sqlalchemy.create_engine(BaseRepository.conn)
        sql = sqlalchemy.text("UPDATE Usuarios SET name = :name, email = :email WHERE id = :id")
        with db.connect() as conn:
            dr = conn.execute(sql,{"id":item.id, "name":item.name, "email":item.email})
            conn.commit()
        return DMLEntity()

    def updateEmail(self,id,email)->UserEntity:
        db = sqlalchemy.create_engine(BaseRepository.conn)
        sql = sqlalchemy.text("UPDATE Usuarios SET email = :email WHERE id = :id")
        with db.connect() as conn:
            dr = conn.execute(sql,{"id": id, "email": email})
            conn.commit()
        return DMLEntity()