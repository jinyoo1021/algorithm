class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        keep = []
        ans = []

        for i in s:
            if i in vowel:
                keep.append(i)
            
        for i in s:
            if i in vowel:
                ans.append(keep.pop(-1))
            else:
                ans.append(i)

        return ''.join(ans)

def main():
    sol = Solution()
    sol = sol.reverseVowels(s = "aA")
    print(sol)

if __name__ == '__main__':
    main()