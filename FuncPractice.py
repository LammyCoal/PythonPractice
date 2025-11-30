def palindrome(word):
    if word.lower() == word[::-1].lower():
        answer = 'This word is a palindrome'
    else:
        answer = 'This word is not a palindrome'
    return answer

print(palindrome('Level'))

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
print(factorial(5))

def largest(integer):
    answer = integer[0]

    for num in integer:
        if num > answer:
            answer = num
    return answer

number = [1, 2, 3, 45, 5]
print(largest(number))
