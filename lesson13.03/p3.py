"""Есть список целых. Необходимо первую половину
списка отсортировать по убыванию, вторую половину
по возрастанию"""

def numbers_sort_1(array: list):
    # Определяем длину половины
    half_length = len(array) // 2
    # Получаем первую половину списка
    first_half = array[:half_length]

    # Возвращаем первую половину списка
    return first_half


def sort_second(array: list):
    # Определяем половину длины списка
    half_length = len(array) // 2
    # Получаем вторую половину списка
    second_half = array[half_length:]

    # Возвращаем вторую половину списка
    return second_half


def sort_first_half(array: list):
    # Внешний цикл для прохода по всем элементам списка
    for i in range(len(array)):
        # Внутренний цикл for для сравнения и обмена соседних элементов, если необходимо
        for j in range(0, len(array) - 1):
            # Если текущий элемент array[j] больше следующего элемента array[j + 1]
            if array[j] > array[j + 1]:
                # Обмен элементов местами с помощью кортежей
                array[j], array[j + 1] = array[j + 1], array[j]

    # Возвращение отсортированного списка
    return list(array)


def sort_second_half(array: list):
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
    return array


array = [3,1,4,6,7,8,2,3,]
# Выводим первую и вторую половину списка
one_strok = numbers_sort_1(array)
two_strok = sort_second(array)
# Сортируем половины и соединяем
result = list(sort_first_half(one_strok) + sort_second_half(two_strok))
print(result)
