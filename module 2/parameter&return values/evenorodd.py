class Number:
    def __init__(self, num):
        self.num = num

    def even_odd(self):
        if self.num % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def prime(self):
        if self.num < 2:
            return "Not Prime"

        for i in range(2, self.num):
            if self.num % i == 0:
                return "Not Prime"

        return "Prime"

    def palindrome(self):
        reverse = str(self.num)[::-1]

        if str(self.num) == reverse:
            return "Palindrome"
        else:
            return "Not Palindrome"


n = Number(121)

print("Number:", n.num)
print("Even/Odd:", n.even_odd())
print("Prime:", n.prime())
print("Palindrome:", n.palindrome())