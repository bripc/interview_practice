lookup = {}


def add_extra(num):
    print("Looking up additional coinage for" , num)
    if num in lookup.keys():
        print("Found.")
        return lookup[num]
    print(num, "not found, breaking num down again.")
    return conversion(num)


def conversion(n):
    by2 = int(n/2)
    by3 = int(n/3)
    by4 = int(n/4)
    print("n divided by 2, 3, and 4:", by2, by3, by4)
    total = by2 + by3 + by4
    print("Total:", total)

    # if the total of dividing it into 3 coins is more than the 1:1 ratio
    if total > n:
        print("Total was greater than n")
        add_to = 0
        add_to += add_extra(by2)
        add_to += add_extra(by3)
        add_to += add_extra(by4)
        lookup[n] = add_to
        return add_to
    else:
        print("Total was less than or equal to n")
        lookup[n] = n
        return n


# print("---------------------------------------------")
# print("12 Bytelandian is $", conversion(12))
# print("---------------------------------------------")
# print("2 Bytelandian is $", conversion(2))
# print("---------------------------------------------")
# print("13 Bytelandian is $", conversion(13))
# print("---------------------------------------------")
# print("100 Bytelandian is $", conversion(100))
# print("---------------------------------------------")
# print("25 Bytelandian is $", conversion(25))
# print("---------------------------------------------")
# print("1003256 Bytelandian is $", conversion(1003256))
# print("---------------------------------------------")
# print("Lookup table was", lookup)

# ------------------------------------------------------------------------------

# Sieve of Eratosthenes for prime number generation
def generate_primes(m, n):
    primes = list(range(2, n + 1))
    global p
    p = 2
    while p <= n:
        print(primes)
        for num in primes:
            if num % p is 0 and num is not p:
                primes.remove(num)

        for next_prime in primes:
            if next_prime > p:
                p = next_prime
                break

    return primes

#print(generate_primes(2, 25))

# ------------------------------------------------------------------------------


def find_palindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        print("Beginning of while, i, j", i, j)
        palindrome_start = i
        palindrome_end = j
        if string[i] is not string[j]:
            i += 1
            palindrome_start = i

        while string[i] is string[j] and i < j:
            print("string[i], string[j]", string[i], string[j])
            print("i, j before increment", i, j)
            i += 1
            j -= 1
            print("i, j after increment", i, j)

        if i is j:
            return string[palindrome_start:palindrome_end + 1]


print(find_palindrome("racecardsafda"))
