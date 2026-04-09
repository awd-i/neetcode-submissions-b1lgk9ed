class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for string in strs:
            sortedS = ''.join(sorted(string))
            try:
                answer[sortedS].append(string)
            except KeyError:
                answer[sortedS] = [string]

        return answer.values()
        