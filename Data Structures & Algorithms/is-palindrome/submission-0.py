class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        new_s = ""

        for char in s:
            if char.isalnum():
                list1.append(char.lower())

        for i in list1:
            new_s = new_s + str(i)

        if new_s == new_s[::-1]:
            return True
        else:
            return False


