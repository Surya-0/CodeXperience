from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        in_hand = {5: 0, 10: 0}
        for bill in bills:
            # print(in_hand)
            if bill == 5:
                in_hand[5] += 1

            elif bill == 10:
                if in_hand[5] == 0:
                    return False

                else:
                    in_hand[5] -= 1
                    in_hand[10] += 1

            else:
                if in_hand[5] == 0:
                    return False

                elif in_hand[5] and in_hand[10]:
                    in_hand[5] -= 1
                    in_hand[10] -= 1

                elif in_hand[5] * 5 >= 15:
                    in_hand[5] -= 3

                else:
                    return False

        return True