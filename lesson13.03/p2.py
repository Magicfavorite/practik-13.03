"""Написать программу, выполняющую сортировку
 списка целых методом вставок"""

def insertion_sort(array):
    array_len = len(array)
    for i in range(1, array_len):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return  array


my_list = [1,4,2,6,3,4,5,3,5]
print(f'отсорт список {insertion_sort(my_list)}')
print(f'неотсорт список {my_list}')
