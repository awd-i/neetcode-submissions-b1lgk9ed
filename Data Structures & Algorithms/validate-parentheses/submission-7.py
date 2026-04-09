class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partners = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for character in s:
            if character in partners:
                if stack and stack[-1] == partners[character]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False
        