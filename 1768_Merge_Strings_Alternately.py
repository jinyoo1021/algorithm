class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])
            i += 1

        return "".join(merge)
        

def main():
    sol = Solution()
    sol = sol.mergeAlternately(word1="ab", word2="pqrs")
    print(sol)

if __name__ == '__main__':
    main()