import time
from typing import Any, Callable


def timer(func) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function name: {func.__name__} \nExecution time: {execution_time} seconds")
        return result

    return wrapper


@timer
def base_script() -> None:
    numbers = [i for i in range(1000001)]
    squares = []
    for number in numbers:
        squares.append(number ** 2)


@timer
def modified_script() -> None:
    """
    Модифицированный скрипт:
    range создает объект-генератор, который не хранит все значения в памяти, а генерирует их по мере необходимости.
    map создает объект-генератор, который применяет анонимную функцию к каждому элементу последовательности возводя в квадрат.
    """
    numbers = range(1000001)
    squares = list(map(lambda x: x ** 2, numbers))

@timer
def modified_script_2() -> None:
    """
    Модифицированный скрипт:
    range создает объект-генератор, который не хранит все значения в памяти, а генерирует их по мере необходимости.
    Аллоцируется память для списка squares, чтобы избежать повторного выделения памяти при добавлении элементов.
    Во время итерации по объекту-генератору numbers, каждое значение возводится в квадрат и добавляется в список squares.
    """
    numbers = range(1000001)
    squares = 1000001*[None]
    for i in numbers:
        squares[i] = i ** 2


if __name__ == "__main__":
    base_script()
    modified_script()
    modified_script_2()
