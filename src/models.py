import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(25), nullable=False)
    lastname = Column (String(25), nullable = False)
    password = Column (String(25), nullable = False )
    email = Column(String(30), unique= True, nullable = False)
    userName = Column (String(30), unique= True, nullable = False)
    subscriptionDate = Column(Date(), nullable = False)


class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False )

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(25), nullable= False)
    lastname = Column (String(25), nullable = False)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False)


class FavoritosPlanetas(Base):
    __tablename__= 'favoritosPlanetas'
    id = Column ( Integer, primary_key = True )
    usuario_id = Column (Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))

class FavoritosPersonajes(Base):
    __tablename__= 'favoritosPersonajes'
    id = Column ( Integer, primary_key = True )
    usuario_id = Column (Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('personajes.id'))

class FavoritosVehiculos(Base):
    __tablename__= 'favoritosVehiculos'
    id = Column ( Integer, primary_key = True )
    usuario_id = Column (Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('vehiculos.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
