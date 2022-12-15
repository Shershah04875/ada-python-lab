ans = []  # List to store all the unique palindromes of the given string


def checkPalindrome(arr):  # Function to check if the passed string is palindrome or not
    i = 0
    j = len(arr) - 1
    if i == j:
        return False
    while i <= j:
        if arr[i] != arr[j]:
            return False

        i = i + 1
        j = j - 1

    return True


def GetSubString(arr):  # Function to generate all substrings possible from given string and
    i = 0  # To check each and every substring that if it is palindrome or not
    # if palindrome then storing it in the ans list if it is not present in the list already
    # global ans

    while i < len(arr):
        j = i
        while j < len(arr):
            if checkPalindrome(arr[i:j+1]):
                #  print(arr[i:j+1])
                if ans.count(arr[i:j+1]) == 0:
                    ans.append(arr[i:j+1])
            j = j + 1
        i = i + 1


arr = "RaviivaR"

# calling GetSubString() function to store all unique palindrome possible from given string
GetSubString(arr)

i = 0
while i < len(ans):  # Loop to print all unique palindrome substring
    print(ans[i])
    i = i + 1
