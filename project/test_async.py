import asyncio
from default.readfile import get_file
from default.db import CepSerial, Session
from time import time
from aiohttp import ClientSession

Session = Session()
ms = CepSerial()


def save_result(result: dict) -> bool:
    try:
        cep = ms.load(result, session=Session)
        Session.add(cep)
        Session.commit()
        return True
    except Exception:
        Session.rollback()
        return False


async def fetch(session: ClientSession, url: str) -> dict:
    headers = {"Accept": "application/json"}
    async with session.get(url, headers=headers) as response:
        return await response.json()


async def get_cep(cep: int = None, number: int = 0) -> None:
    url = f"http://cep.la/{cep}"
    async with ClientSession() as client:
        result = await fetch(session=client, url=url)
    if not result:
        print(f"Erro ao buscar CEP: {number} - cep: {cep}")
    else:
        if type(result) == list:
            result = result[0]
        insert = save_result(result)
        print(
            f"Inserido com sucesso: {number} - cep: {cep}"
            if insert
            else f"Erro ao inserir: {number} - cep: {cep}"
        )


async def execute() -> None:
    ceps = get_file()
    lista = list()
    for i, cep in enumerate(ceps):
        lista.append(get_cep(cep=cep, number=i))

    await asyncio.wait(lista)


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(execute())
    loop.close()

