from ting_file_management.priority_queue import PriorityQueue
import pytest


def factory_mock(file_name: str, lines: list):
    return {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }


def test_basic_priority_queueing():
    file1_p = factory_mock("file1.txt", ["Trybe", "is", "not", "Google"])
    file2_p = factory_mock("file2.txt", ["a", "good", "book"])
    file3_np = factory_mock("file3.txt", ["The", "book", "on", "the", "table"])

    queue = PriorityQueue()
    queue.enqueue(file3_np)
    queue.enqueue(file1_p)
    queue.enqueue(file2_p)

    with pytest.raises(IndexError):
        queue.search(-1)

    assert len(queue) == 3
    assert queue.search(0) == file1_p
    assert queue.search(1) == file2_p
    assert queue.search(2) == file3_np

    with pytest.raises(IndexError):
        queue.search(3)

    assert queue.dequeue() == file1_p
    assert queue.dequeue() == file2_p
    assert queue.dequeue() == file3_np
