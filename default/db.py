from sqlalchemy import Table, String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


url = "sqlite:///default/db.db"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CepModel(Base):
    __tablename__ = "ceps"
    uf = Column(String(255), nullable=True)
    gia = Column(String(255), nullable=True)
    cep = Column(String(255), primary_key=True)
    ibge = Column(String(255), nullable=True)
    bairro = Column(String(255), nullable=True)
    unidade = Column(String(255), nullable=True)
    localidade = Column(String(255), nullable=True)
    logradouro = Column(String(255), nullable=True)
    complemento = Column(String(255), nullable=True)

    def __repr__(self):
        return '<Example model {}>'.format(self.cep)
    


class CepSerial(SQLAlchemySchema):
    class Meta:
        model = CepModel
        load_instance = True
    
    uf = auto_field()
    cep = auto_field()
    gia = auto_field()
    ibge = auto_field()
    bairro = auto_field()
    unidade = auto_field()
    logradouro = auto_field()
    localidade = auto_field()
    complemento = auto_field()




class CepModel2(Base):
    __tablename__ = "enderecos"
    uf = Column(String(255), nullable=True)
    cep = Column(String(255), primary_key=True)
    bairro = Column(String(255), nullable=True)
    cidade = Column(String(255), nullable=True)
    logradouro = Column(String(255), nullable=True)


    def __repr__(self):
        return '<Example model {}>'.format(self.cep)

class CepSerial2(SQLAlchemySchema):
    class Meta:
        model = CepModel2
        load_instance = True
    
    uf = auto_field()
    cep = auto_field()
    bairro = auto_field()
    cidade = auto_field()
    logradouro = auto_field()
        

Base.metadata.create_all(engine)