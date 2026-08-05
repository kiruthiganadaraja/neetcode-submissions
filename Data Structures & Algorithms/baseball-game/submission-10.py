class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        final_value = 0
        for opr in operations:
            if opr == "+":
                record.append(record[-1] + record[-2])
                print(record)
            elif opr =="C":
                 record.pop()
                 print(record)
            elif opr == "D":
                 value = 2*record[-1]
                 record.append(value)
                 print(record)
            else:
                record.append(int(opr))
                print(record)
        return sum(record)

