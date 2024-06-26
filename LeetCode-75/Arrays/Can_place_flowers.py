class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: int) -> bool:

        for i in range(len(flowerbed)):
            if n == 0:
                return True

            if flowerbed[i] == 0:
                if i > 0 and i < len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        # print("The val is : ",i)
                        flowerbed[i] = 1
                        n -= 1

                elif i == 0:
                    if len(flowerbed) > 1:
                        if flowerbed[i + 1] == 0:
                            # print("The val is pi : ",i)
                            flowerbed[i] = 1
                            n -= 1
                    else:
                        # print("The val is : ",i)
                        flowerbed[i] = 1
                        n -= 1

                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        # print("The val is : ",i)
                        flowerbed[i] = 1
                        n -= 1

        # print(n)
        return n == 0