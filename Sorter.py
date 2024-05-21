NoOfWords = int(input("Enter the number of words: "))
words = []
FWord = input("Enter the first word: ")
words.append(FWord)
while len(words) != NoOfWords:
    NWord = input("Enter the next word: ")
    words.append(NWord)
Order = input("Which order do you prefer: \n 1. Ascending Order   \n  2. Descending Order  \n >>> ")
if int(Order) == 1:
    words.sort()
    print(words)
else:
    words.sort(reverse=True)
    print(words)