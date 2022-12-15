def AllPermutation(word):  # Function to compute all the possible string from three letter word
    ans1 = []  # Declaring empty string to store all permutation of the given word
    for i in range(len(word)):
        for j in range(len(word)):
            if i == j:
                continue  # Skipping inner k loop if i and j are pointing to the same letter of the given word
            for k in range(len(word)):
                if j == k or k == i:  # skipping the current iteration of the k loop if i or j and k are pointing to the same letter
                    continue
                # Appending the word in which i not equals to j nor k
                ans1.append(word[i]+word[j]+word[k])
    return ans1  # Finally returning our answer which is stored in the list ans1

#Driver Program

myWord = input("Enter your string : ")  # Taking input from the user
# calling AllPermutatin() function which returns our required answer
ans = AllPermutation(myWord)

print(ans)  # printing our answer
