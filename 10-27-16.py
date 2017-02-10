import random

print("Hello Bri! You're going to great on your interview!")
print("Starting with something easy...")

arr = [34, 56, 20, -10, 44, 9, 66, 7]

print("Selection sort")

print("Unsorted array:", arr)

# Scans the given elements to find smallest element,
# exchanges it with the first. Scans for the second smallest
# and exchanges it with the second, etc.

for i in range(len(arr)):
    smallestIndex = i
    for j in range(i, len(arr)):
        if arr[smallestIndex] > arr[j]:
            smallestIndex = j
    arr[i], arr[smallestIndex] = arr[smallestIndex], arr[i]

print("Sorted:", arr)

print("--------------------------------------------------------")

print("Binary search")

# Look at the middle element of the list. Is it the element you want? No?
# Is the list only one element?
# Is it less than or greater than? Look at the list that corresponds to the less
# than or greater than list and recursively do this.


def binary_search(items, target):
    length = len(items)
    middleIdx = int(length/2)
    middleVal = items[middleIdx]

    if length is 1:
        if items[middleIdx] is target:
            print(middleVal, "found")
            return middleVal
        else:
            print(target, "not found")
            return False

    if middleVal is target:
        print(middleVal, "found")
        return middleVal
    elif middleVal < target:
        return binary_search(items[middleIdx+1:length], target)
    elif middleVal > target:
        return binary_search(items[0:middleIdx], target)
    else:
        print(target, "not found")
        return False


print("Searching for 56")
binary_search(arr, 56)
print("Searching for 55")
binary_search(arr, 55)

random.shuffle(arr)

print("--------------------------------------------------------")

print("Mergesort")

print("Before sorting", arr)


def merge(left, right):
    sorted = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))
    if len(left) > 0:
        for item in left:
            sorted.append(item)
    if len(right) > 0:
        for item in right:
            sorted.append(item)
    return sorted


def mergesort(items):
    if len(items) == 1:
        return items

    left = items[0:int(len(items)/2)]
    right = items[int(len(items)/2):len(items)]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

print("sorted array", mergesort(arr))

print("--------------------------------------------------------")

print("String Manip practice")
print("Finding all duplicate characters")

str = "Look I'm a string with lots of letters!"
str = str.replace(" ", "")
dups = {}

for ch in str:
    if ch not in dups:
        dups[ch] = 1
    else:
        dups[ch] += 1
print("Duplicate characters:")
for letter in dups:
    if dups[letter] > 1:
        print(letter, end=", ")

print("\n--------------------------------------------------------")

print("Are they anagrams?")
anagram1 = "army"
anagram2 = "mary"
anagram3 = "cat"

alpha1 = "".join(sorted(anagram1))
alpha2 = "".join(sorted(anagram2))
alpha3 = "".join(sorted(anagram3))

print("Answer:", alpha1 == alpha2)
print("Answer:", alpha1 == alpha3)

print("--------------------------------------------------------")

print("Is it a palindrome?")
pali1 = "racecar"
pali2 = "not a palindrome"


def pali_check(str):
    length = len(str)
    for i in range(0, int(length/2)):
        if str[i] != str[length-1-i]:
            return False
    return True

print(pali1, "is a palindrome", pali_check(pali1))
print(pali2, "is a palindrome", pali_check(pali2))

print("--------------------------------------------------------")

print("Recursively finding the count of a character in a string")


# returns how many times that character is in the string
def find_count(str, char):
    if len(str) == 0:
        return 0
    if str[0] == char:
        return find_count(str[1:], char) + 1
    else:
        return find_count(str[1:], char)


print("Finding how many o's are in 'Hello World'", find_count("Hello World!", 'o'))