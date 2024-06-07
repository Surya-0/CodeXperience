from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for c in string:
            count[ord(c) - ord('a')] += 1
        print(tuple(count)," ",d[tuple(count)])
        d[tuple(count)].append(string)

    return d.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
