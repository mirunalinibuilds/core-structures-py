class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        for i in range(left, right + 1):

            is_self_dividing = True
            digits = [int(char) for char in str(i)]

            for digit in digits:

                if digit == 0 or i % digit != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                self_dividing_nums.append(i)

        return self_dividing_nums
