# Напистаь программу, выполняющую сортировку
# списка целых методом пузырьковой сортировкой

def bubble_sort(array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(0,array_len - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

my_list = [1,4,2,6,3,4,5,3,5]
print(f'неотсорт список {my_list}')
print(f'отсорт список {bubble_sort(my_list)}')







