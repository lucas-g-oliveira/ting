from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    for i in range(len(instance)):
        if path_file == instance.search(i)["nome_do_arquivo"]:
            return instance.search(i)

    data = txt_importer(path_file)
    instance.enqueue(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
    )
    print(instance.search(len(instance) - 1), file=sys.stdout)
    return


def remove(instance: Queue):
    if not len(instance):
        print("Não há elementos", file=sys.stdout)
    else:
        item = instance.dequeue()
        print(
            f"Arquivo {item['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
