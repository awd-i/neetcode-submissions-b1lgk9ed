from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # make a default dict of the groups
        for s in strs:
            key = tuple(sorted(s)) # return a sorted list of characters, make that the key
            groups[key].append(s) # append the string to the key
        return list(groups.values()) # return a list of the values in the dictionary