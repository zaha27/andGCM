#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



// Bubble Sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

// Binary Search
int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> data = {5, 2, 9, 1, 5, 6};
    bubbleSort(data);
    for (int num : data) cout << num << " ";
    cout << "\nIndex of 5: " << binarySearch(data, 5) << endl;
    return 0;
}
