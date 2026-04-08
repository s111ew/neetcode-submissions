class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "[": "]",
            "(": ")",
            "{": "}",
        }
        stack = Stack()
        openers = pairs.keys()
        for char in s:
            if char in openers:
                stack.append_to_head(char)
            else:
                if stack.get_head_val() is None or char != pairs[stack.get_head_val()]:
                    return False
                else:
                    stack.remove_from_head()
        return stack.get_head_val() == None

class Stack:
    def __init__(self):
        self.head = None

    def get_head_val(self):
        if self.head is None:
            return None
        return self.head["val"]

    def append_to_head(self, val):
        curr_head = self.head
        new_head = {
            "val": val, 
            "next": curr_head
        }
        self.head = new_head

    def remove_from_head(self):
        if self.head != None:
            self.head = self.head["next"]
