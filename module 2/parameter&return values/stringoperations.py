class StringOperations:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

    def count_vowels(self):
        count = 0

        for ch in self.text.lower():
            if ch in "aeiou":
                count = count + 1

        return count

    def palindrome(self):
        if self.text == self.text[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"


s = StringOperations("madam")

print("Original:", s.text)
print("Reverse:", s.reverse())
print("Vowels:", s.count_vowels())
print("Palindrome:", s.palindrome())