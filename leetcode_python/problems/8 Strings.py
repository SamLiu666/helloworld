
"""https://leetcode.com/tag/string/"""
import re
from typing import List


class Solution:

    # 1108. Defanging an IP Address
    def defangIPaddr(self, address: str) -> str:
        # use the string function to replace you want to replace
        return address.replace(".", "[.]")

    # 1221. Split a String in Balanced Strings
    def balancedStringSplit(self, s: str) -> int:
        # just count, if char is R +1, or -1, then if count==0, means a pair,so ans += 1
        st, res, flag = list(s), [], 0
        ans = 0
        for ch in s:
            if ch =='L':
                flag += 1
            if ch =='R':
                flag -= 1
            if flag == 0:
                ans += 1
        return ans

    # 709. To Lower Case
    def toLowerCase(self, str: str) -> str:
        return str.lower()

    # 1370. Increasing Decreasing String
    def sortString(self, s: str) -> str:
        pass

    # 804. Unique Morse Code Words
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # use hashset
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        char = {}
        for word in words:
            res = []
            for ch in word:
                res.append(morse[ord(ch) - ord('a')])
            code = "".join(res)
            # char[word] = code
            char[code] = word
        print(char)
        return len(char.values())

    # 1309. Decrypt String from Alphabet to Integer Mapping
    def freqAlphabets(self, s: str) -> str:
        # re.findall()在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        match = re.findall(r'\d\d#|\d', s)
        print(match)
        ans = ""
        for n in match:
            ans +=chr(int(n[:2])+96)
        return ans


if __name__ == '__main__':
    s = Solution()
    # address = "1.1.1.1"     # 1108.
    # n = "RLRRLLRLRL"  # 1221
    # n = "Hello"
    # words = ["gin", "zen", "gig", "msg"]  #
    words = "10#11#12"
    ans = s.freqAlphabets(words)
    print(ans)