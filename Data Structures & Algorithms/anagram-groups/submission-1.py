class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for string in strs:
            sortedS = ''.join(sorted(string))
            answer[sortedS].append(string)


        return answer.values()
        