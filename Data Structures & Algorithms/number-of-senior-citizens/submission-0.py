class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            if int(passenger[11]) > 6:
                count += 1
            if int(passenger[11]) == 6:
                if int(passenger[12]) > 0:
                    count += 1
        return count