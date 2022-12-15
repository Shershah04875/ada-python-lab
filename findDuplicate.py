def isPresent(arr, start: int, end: int, index: int):  #Applying binary search to find duplicate of given index
    if (start > end):
        return False
    mid = int((start + end) / 2)
    if arr[mid] == arr[index]:
        return True
    elif arr[mid] > arr[index]:
        return isPresent(arr, start, mid - 1, index)
    else:
        return isPresent(arr, mid + 1, end, index)


def PrintDuplicates(arr, n):  #Function to cover all elements of the list
    for i in range(0,n):
        if isPresent(arr, i+1, n-1, i): #Checking if duplicate of index i is present or not
            print(arr[i], end=" ")    #if present then printing that particular duplicate element


if __name__ == "__main__" :
    list = [] #Declaring an array with the name list of empty size
    n = int(input("Enter size of your list: "))  #Asking for size of array
    print("Enter all elements of your list one by one:")
    
    for i in range(0,n):        #Running a loop to take all element from user 
        element = int(input())
        list.append(element)
    list.sort()    #Sorting the given array
    print("All duplicate elements present in the list is :")
    PrintDuplicates(list, n)  #Calling the main Function
