from sqlalchemy import String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


uri = "sqlite:///default/db.db"
engine = create_engine(uri)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class CepModel(Base):
    __tablename__ = "enderecos"
    uf = Column(String(255), nullable=True)
    cep = Column(String(255), primary_key=True)
    bairro = Column(String(255), nullable=True)
    cidade = Column(String(255), nullable=True)
    logradouro = Column(String(255), nullable=True)

    def __repr__(self):
        return "<Example model {}>".format(self.cep)


class CepSerial(SQLAlchemySchema):
    class Meta:
        model = CepModel
        load_instance = True

    uf = auto_field()
    cep = auto_field()
    bairro = auto_field()
    cidade = auto_field()
    logradouro = auto_field()


Base.metadata.create_all(engine)
