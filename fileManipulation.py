import pickle

def read_file(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def write_file(filename, obj):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
