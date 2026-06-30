class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        if s[right] == "?":
            right -= 1
        while left < right:
            if (s[left] == "," or s[left] == "'" or s[left] == "." or s[left] == ":"):
                left += 1
            elif (s[right] == "," or s[right] == "'" or s[right] == "." or s[right] == ":"):
                right -= 1
            elif s[left] != " " and s[right] == " ":
                right -= 1
            elif s[right] != " " and s[left] == " ":
                left += 1
            elif s[left].lower() == s[right].lower():
                print(s[left].lower())
                print(s[right].lower())
                left += 1
                right -= 1

            else:
                return False
        return True