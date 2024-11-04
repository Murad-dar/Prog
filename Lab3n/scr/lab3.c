#include <stdio.h>
#include <limits.h>

void processArray(int arr[], int size) {
    int minIndex = 0;
    int maxIndex = 0;
    int minValue = arr[0];
    int maxValue = arr[0];

    // Найти индексы и значения минимума и максимума
    for (int i = 1; i < size; i++) {
        if (arr[i] < minValue) {
            minValue = arr[i];
            minIndex = i;
        }
        if (arr[i] > maxValue) {
            maxValue = arr[i];
            maxIndex = i;
        }
    }

    // Найти сумму индексов
    int indexSum = minIndex + maxIndex;

    // Сравнить сумму индексов с минимумом и максимумом
    if (indexSum < minValue) {
        arr[minIndex] = indexSum; // Записать на место минимума
    } else if (indexSum > maxValue) {
        arr[maxIndex] = indexSum; // Записать на место максимума
    } else {
        // Обнулить массив между минимумом и максимумом
        int start = minIndex < maxIndex ? minIndex : maxIndex;
        int end = minIndex > maxIndex ? minIndex : maxIndex;

        for (int i = start + 1; i < end; i++) {
            arr[i] = 0;
        }
    }
}

int main() {
    int arr[] = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    processArray(arr, size);

    // Вывод результата
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
