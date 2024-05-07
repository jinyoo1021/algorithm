class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bool_list = []


        for i in range(len(candies)):
            
            if candies[i] + extraCandies >= max(candies):
                bool_list.append(True)
            else:
                bool_list.append(False)
        
        return bool_list
        


def main():
    sol = Solution()
    sol = sol.kidsWithCandies(candies = [12,1,12], extraCandies = 10)
    print(sol)

if __name__ == '__main__':
    main()