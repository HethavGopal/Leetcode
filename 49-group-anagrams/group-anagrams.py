class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            temp_dict[sorted_word].append(word)

        return list(temp_dict.values())