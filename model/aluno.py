from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Aluno(Base):
    __tablename__ = 'aluno'

    id = Column("pk_aluno", Integer, primary_key=True)
    nome = Column(String(255), unique=False)
    documento = Column(String(255), unique=True)
    genero = Column(String(255), unique=False)
    data_nascimento = Column(String(255), unique=False)
    email = Column(String(255), unique=False)
    telefone = Column(String(255), unique=False)

    def __init__(self, nome:str, documento:str, genero:str,
                 data_nascimento:str, email:str, telefone:str):
        """
        Cria um Aluno

        Arguments:
            nome: nome do aluno.
            documento: documento de identificação do aluno
            genero: genero do produto
            data_nascimento: data de nascimento do aluno
            email: email do aluno
            telefone: telefone do aluno
        """
        self.nome = nome
        self.documento = documento
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
