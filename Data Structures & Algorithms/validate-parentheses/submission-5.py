class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partners = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for character in s:
            if character in partners:
                if stack and stack.pop() == partners[character]:
                    continue
                else:
                    return False
            else:
                stack.append(character)
        if not stack:
            return True
        else:
            return False

        