class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unq = set()
        for e in emails:
            unq.add(self.absoluteAddress(e))
        return len(unq)
        
    def absoluteAddress(self, email: str) -> str:
        out = ""
        i = 0
        n = len(email)-1
        # collect local addr up to '+' or '@'
        while i <= n and email[i] != "@":
            char = email[i]

            if char == "+":
                break

            if char != ".":
                out += char
            
            i+=1
        
        # get to '@'
        while i <= n and email[i] != "@":
            i+=1
        
        # append domain addr
        out += email[i:]
        return out