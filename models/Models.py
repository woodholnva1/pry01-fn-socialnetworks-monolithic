# coding: utf-8
from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
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


class RegistroForm(Base):
    __tablename__ = 'registro_form'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False)
    edad = Column(Integer, nullable=False)
    redPreferida = Column(Text, nullable=False)
    TmpFacebook = Column(Text, nullable=False)
    TmpWhasap = Column(Text, nullable=False)
    TmpTwitter = Column(Text, nullable=False)
    TmpInsta = Column(Text, nullable=False)
    Tmptiktok = Column(Text, nullable=False)
    sexo = Column(Text, nullable=False)


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
