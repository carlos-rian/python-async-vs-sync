import os

dir_real = os.path.realpath(".")


def get_file():
    path = os.path.join(dir_real, "default/CEPs.txt")
    with open(file=path, encoding="utf-8", mode="r") as cep:
        ceps = cep.read().split("\n")
    return ceps
