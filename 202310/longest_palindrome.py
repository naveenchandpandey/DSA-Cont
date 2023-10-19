
class LongestPalindrome:
    def __init__(self, input_str: str) -> None:
        self.input_str = input_str
        self.result = None

    def get_palindrome_result(self, left: int, right: int) -> str:
        while left >= 0 and right < len(self.input_str) and self.input_str[left] == self.input_str[right]:
            if len(self.input_str[left: right + 1]) > len(self.result):
                self.result = self.input_str[left: right + 1]
            left -= 1
            right += 1

    def find_longest_palindrome(self):
        self.result = ''
        for i in range(0, len(self.input_str)):
            left, right = i, i
            self.get_palindrome_result(left, right)
            left, right = i, i+1
            self.get_palindrome_result(left, right)

        return self.result


if __name__ == '__main__':
    longest_palindrome = LongestPalindrome('zabcbaf')
    print(longest_palindrome.find_longest_palindrome())
    longest_palindrome = LongestPalindrome('zabccbaf')
    print(longest_palindrome.find_longest_palindrome())
