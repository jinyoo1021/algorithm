# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (flowerbed[0] == 0):
                if len(flowerbed) == 1:
                    return True
                elif (flowerbed[1] == 0):
                    n -= 1
                    flowerbed[0] = 1
                flowerbed[0] = 1

            elif (flowerbed[i-1] == 0) and (flowerbed[i] == 0) and (flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
            elif (flowerbed[-1] == 0) and (flowerbed[-2] == 0):
                n -= 1
                flowerbed[-1] = 1

        if n <= 0:
            return True
        else:
            return False

def main():
    sol = Solution()
    sol = sol.canPlaceFlowers(flowerbed = [0,1,0,1,0,1,0,0], n = 1)
    print(sol)

if __name__ == '__main__':
    main()