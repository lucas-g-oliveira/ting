import sys


def txt_importer(path_file):
    print(str(path_file).split(".")[-1])
    if not str(path_file).split(".")[-1] == "txt":
        print("Formato inválido", file=sys.stderr)
        return []
    try:
        with open(path_file, "r") as file:
            content = file.read().split("\n")
            return content
    except Exception:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
