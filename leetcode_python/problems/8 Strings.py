
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
        # re.findall() find all the element fitting the pattern, return them as a list。
        match = re.findall(r'\d\d#|\d', s)
        print(match)
        ans = ""
        for n in match:
            ans +=chr(int(n[:2])+96)
        return ans

    # 1374. Generate a String With Characters That Have Odd Counts
    def generateTheString(self, n: int) -> str:
        # odd times
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n-1) + 'b'

    # 657. Robot Return to Origin
    def judgeCircle(self, moves: str) -> bool:
        # left right  up down
        # count = 0
        # direction = {"U": 2, "D": -2, "L": 1, "R": -1}
        # for m in moves:
        #     count += direction[m]
        # return count == 0
        l,r,u,d = moves.count('L'),moves.count('R'),moves.count('U'), moves.count('D')
        return l==r and u==d

    # 557. Reverse Words in a String III
    def reverseWords(self, s: str) -> str:
        ans = " "
        return " ".join(word[::-1] for word in s.split(" "))
            # ans += word[::-1]

    # 929. Unique Email Addresses
    def numUniqueEmails(self, emails: List[str]) -> int:
        # def name_email(name, domains):
        #     dic = {}
        #     if domains.count(".") != 1 or domains.count('+') != 0:
        #         return 0
        #     else:
        #         domain = domains
        #     person = name.split("+")
        #     dic[person[1]] = domain  # person for address
        person_mail = set()
        for email in emails:
            name, domains = email.split("@")
            local = name.split("+")[0].replace(".", "")
            person_mail.add(local + "@" + domains)
        return len(person_mail)



if __name__ == '__main__':
    s = Solution()
    # address = "1.1.1.1"     # 1108.
    # n = "RLRRLLRLRL"  # 1221
    # n = "Hello"
    # words = ["gin", "zen", "gig", "msg"]  #
    # words = "10#11#12"
    # ans = s.freqAlphabets(words)
    # n = 2
    # ans = s.generateTheString(n)
    # ss = "LDRRLRUULR"
    # n = "Let's take LeetCode contest"
    l = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    ans = s.numUniqueEmails(l)
    print(ans)