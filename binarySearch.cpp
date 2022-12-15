#include <iostream>
using namespace std;

int BinarySearch(int arr[], int i, int j, int key)      // Function for Binary Search using Recursion Concept
{
    if (i > j)                                         // Condition for Element not exist-->>if Executed then element not exist
        return -1;
    else
    { 
        int mid = (i + j) / 2;                       // Calculating middle index of array
        if (arr[mid] == key)                        // Checking if middle index element is equals to key or not
            return mid;

        if (arr[mid] > key)                         // checking if key is less than middle element, if yes then check left half part of array
            return BinarySearch(arr, i, mid - 1, key);
        else                                           // if key if greater than middle element, search in right half of the array
            return BinarySearch(arr, mid + 1, j, key);
    }
}

int main()
{
    int arr[10];
    for (int i = 0; i < 10; i++)
    {
        arr[i] = i + 3;
    }

    int key = 15;

    int index = BinarySearch(arr, 0, 9, key);   //storing index returned by BinarySearch() function
    if (index < 0)                             //Checking if index valid or not
        cout << "Error: Key = " << key << " does not exist in the array" << endl;
    else
        cout << "Key = " << key << " is found at position/index " << index << " in the array" << endl;
    return 0;
}