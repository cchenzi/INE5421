# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

import pickle


def read_file(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


def write_file(filename, obj):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
