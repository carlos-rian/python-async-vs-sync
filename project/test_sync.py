import requests
from default.readfile import get_file
from default.db import CepSerial, Session
from time import time

session = Session()


def get_cep(cep: str = None) -> dict:
    url = f"http://cep.la/{cep}"
    headers = {"Accept": "application/json"}
    result: dict = requests.api.get(url=url, headers=headers)
    try:
        result = result.json()
    except Exception:
        result = {"erro": True}
    return result


def save_result(result: dict) -> bool:
    ms = CepSerial()
    try:
        cep = ms.load(result, session=session)
        session.add(cep)
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False


def main() -> None:
    ceps = get_file()
    for i, cep in enumerate(ceps):
        result = get_cep(cep=cep)
        if "erro" not in result:
            insert = save_result(result=result)
            print(
                f"Inserido com sucesso: {i} - cep: {cep}"
                if insert
                else f"Erro ao inserir: {i} - cep: {cep}"
            )
        else:
            print(f"Erro ao buscar CEP: {i} - cep: {cep}")
   
