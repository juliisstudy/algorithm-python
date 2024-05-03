# Input: s = "the sky is blue"
# Output: "blue is sky the"

def reverseWords(self,s:str)->str:
    return " ".join(reversed(s.split()))


