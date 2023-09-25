from pydantic import BaseModel
from typing import Optional, List
from model.aluno import Aluno

class AlunoSchema(BaseModel):
    """ Define como um novo aluno a ser inserido deve ser representado
    """
    nome: str = "Renato Julio Elias Gomes"
    documento: str = "13217432703"
    genero: str = "Masculino"
    data_nascimento: str = "10/06/1981"
    email: str = "renato_julio_gomes@bmalaw.com.br"
    telefone: str = "(82) 99485-8761"

class AlunoUpdateSchema(BaseModel):
    """ Define como um aluno a ser atualizado deve ser representado
    """
    nome: str
    documento: str
    genero: str
    data_nascimento: str
    email: str
    telefone: str

class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no documento do aluno.
    """
    documento: str = "13217432703"

class ListagemAlunoSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    alunos:List[AlunoSchema]

def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "nome": aluno.nome,
            "documento": aluno.documento,
            "genero": aluno.genero,
            "data_nascimento": aluno.data_nascimento,
            "email": aluno.email,
            "telefone": aluno.telefone,
        })

    return {"alunos": result}

class AlunoViewSchema(BaseModel):
    """ Define como um aluno será retornado: aluno + notas.
    """
    id: int = 1
    nome: str = "Renato Julio Elias Gomes"
    documento: str = "13217432703"
    genero: str = "Masculino"
    data_nascimento: str = "10/06/1981"
    email: str = "renato_julio_gomes@bmalaw.com.br"
    telefone: str = "(82) 99485-8761"

class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "documento": aluno.documento,
        "genero": aluno.genero,
        "data_nascimento": aluno.data_nascimento,
        "email": aluno.email,
        "telefone": aluno.telefone
    }