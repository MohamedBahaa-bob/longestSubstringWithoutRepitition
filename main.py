# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0]*107
        maxCount = 0
        l = 0
        r = 0
        while r < len(s):
            if chars[ord(s[r]) - 20] == 0:
                chars[ord(s[r]) - 20] = 1
            else:
                maxCount = max(r - l, maxCount)
                while s[l] != s[r]:
                    chars[ord(s[l]) - 20] = 0
                    l += 1
                l += 1
            r += 1
        return max(r - l, maxCount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring("tmmz~uxt"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
