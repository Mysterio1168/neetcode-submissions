class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # array of alphabets a...z
            for c in s:
                count[ord(c) - ord("a")] += 1 # increments the value of each occurence of the letter

            result[tuple(count)].append(s)  # since cant use array as key  
        return list(result.values())
