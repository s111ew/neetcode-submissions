class Solution:
    def encode(self, strs):
        res = ""
        for string in strs:
            res += str(len(string)) + ","

        res += "#"

        for string in strs:
            res += string

        return res

    def decode(self, string):
        lengths = []
        res = []
        delimeter_idx = 0

        curr_num = ""
        for i in range(len(string)):
            if string[i] == ",":
                lengths.append(int(curr_num))
                curr_num = ""
            elif string[i] == "#":
                delimeter_idx = i+1
                break
            else:
                curr_num += string[i]

        length_total = delimeter_idx
        for l in lengths:
            res.append(string[length_total:length_total+l])
            length_total += l
        return res