//binary
#include <stdio.h>

int binarySearch(int arr[], int size, int target) {
    int l = 0, r = size - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2; // To avoid overflow

        if (arr[mid] == target) {
            return mid; // Target found
        } else if (arr[mid] < target) {
            l = mid + 1; // Search in the right half
        } else {
            r = mid - 1; // Search in the left half
        }
    }
    return -1; // Target not found
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {1, 2, 4, 6, 7, 8, 11, 13, 16, 23};
    int target = 11;
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Array: ");
    printArray(arr, size);

    int result = binarySearch(arr, size, target);

    if (result != -1) {
        printf("Element found at index: %d\n", result);
    } else {
        printf("Element not found.\n");
    }

    return 0;
}

