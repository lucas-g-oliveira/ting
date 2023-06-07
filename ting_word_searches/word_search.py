from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []
    for file in range(len(instance)):
        ocorrencias = []
        lines = instance.search(file)["linhas_do_arquivo"]

        for line_index in range(len(lines)):
            if str(word).lower() in str(lines[line_index]).lower():
                ocorrencias.append({"linha": line_index + 1})

        if len(ocorrencias):
            result.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(file)["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result


def search_by_word(word, instance: Queue):
    result = []
    for file in range(len(instance)):
        ocorrencias = []
        lines = instance.search(file)["linhas_do_arquivo"]

        for line_index in range(len(lines)):
            if str(word).lower() in str(lines[line_index]).lower():
                ocorrencias.append(
                    {"linha": line_index + 1, "conteudo": lines[line_index]}
                )

        if len(ocorrencias):
            result.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(file)["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result
