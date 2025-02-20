from sqlmodel import SQLModel, Field, create_engine, Relationship
from enum import Enum
from datetime import date
from typing import Optional, List


# Definição correta dos Enums (herdando de str)
class Bancos(str, Enum):
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'

class Status(str, Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'

class Tipos(str, Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saida'


class Conta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Permite autoincremento
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

    # Relacionamento com Histórico
    historicos: List["Historico"] = Relationship(back_populates="conta")


class Historico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Permite autoincremento
    conta_id: int = Field(foreign_key="conta.id")
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date

    # Relacionamento com Conta
    conta: Conta = Relationship(back_populates="historicos")


# Configuração do banco de dados SQLite
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)

# Criando as tabelas no banco de dados
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)