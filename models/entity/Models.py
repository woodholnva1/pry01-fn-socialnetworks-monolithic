# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class HoraRede(Base):
    __tablename__ = 'hora_redes'

    id_horas_redes = Column(Integer, primary_key=True)
    descripcion = Column(Text)
    status = Column(Integer)


class RedesSociale(Base):
    __tablename__ = 'redes_sociale'

    id_red_social = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    descripcion = Column(Text)
    status = Column(Integer)


class Sexo(Base):
    __tablename__ = 'sexo'

    id_sexo = Column(Integer, primary_key=True)
    name = Column(Text)
    descripcion = Column(Text)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class RegistroForm(Base):
    __tablename__ = 'registro_form'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False)
    edad = Column(Text, nullable=False)
    redPreferida = Column(ForeignKey('redes_sociale.id_red_social'), nullable=False)
    sexo = Column(ForeignKey('sexo.id_sexo'), nullable=False)

    redes_sociale = relationship('RedesSociale')
    sexo1 = relationship('Sexo')


class RelFormRedesHr(Base):
    __tablename__ = 'rel_form_redes_hrs'

    id_rel_form_redes_hrs = Column(Integer, primary_key=True)
    id_form = Column(ForeignKey('registro_form.id'), nullable=False)
    id_red = Column(ForeignKey('redes_sociale.id_red_social'), nullable=False)
    id_hora = Column(ForeignKey('hora_redes.id_horas_redes'), nullable=False)

    registro_form = relationship('RegistroForm')
    hora_rede = relationship('HoraRede')
    redes_sociale = relationship('RedesSociale')
