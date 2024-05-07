class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        if len(str2) > len(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])

        return str1


def main():
    sol = Solution()
    sol = sol.gcdOfStrings(str1="LEET", str2="CODE")
    print(sol)

if __name__ == '__main__':
    main()