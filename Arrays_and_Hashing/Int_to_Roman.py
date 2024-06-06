class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
             900: 'CM', 1000: 'M'}
        res = ""
        # print(d[1000]+d[500])
        while num > 0:
            # print(num)
            if num >= 1000:
                # print("yes")
                num = num - 1000
                res += d[1000]

            elif num >= 500 and num < 1000:
                if (num // 100) == 9:
                    num = num - 900
                    res += d[900]

                else:
                    num = num - 500
                    res += d[500]

            elif num >= 100 and num < 500:
                if (num // 100) == 4:
                    num = num - 400
                    res += d[400]

                else:
                    num = num - 100
                    res += d[100]

            elif num >= 50 and num < 100:
                if (num // 10) == 9:
                    num = num - 90
                    res += d[90]

                else:
                    num = num - 50
                    res += d[50]


            elif num >= 10 and num < 50:
                if (num // 10) == 4:
                    num = num - 40
                    res += d[40]

                else:
                    num = num - 10
                    res += d[10]

            elif num >= 5 and num < 10:
                if num == 9:
                    num = 0
                    res += d[9]

                else:
                    num = num - 5
                    res += d[5]

            else:
                if num == 4:
                    num = 0
                    res += d[4]

                else:
                    num = num - 1
                    res += d[1]

            # print(num," ",num//10)

        return res