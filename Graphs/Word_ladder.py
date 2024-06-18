from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        if endWord not in wordList:
            return 0
        refer_set = set()
        for i in range(97, 123):
            refer_set.add(chr(i))

        temp_q = deque()
        visit = set()
        wordList = set(wordList)

        # We should add the word and the number of transformations
        temp_q.append((beginWord, 1))
        visit.add(beginWord)

        while temp_q:
            word, moves = temp_q.popleft()
            if word == endWord:
                return moves

            for i in range(len(word)):
                for j in refer_set:
                    new_word = word[:i] + j + word[i + 1:]
                    if new_word in wordList and new_word not in visit:
                        # print(new_word," ",moves+1)
                        temp_q.append((new_word, moves + 1))
                        visit.add(new_word)

        return 0


