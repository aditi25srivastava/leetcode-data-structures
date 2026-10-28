from collections import deque
from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        parents = defaultdict(set)  
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
    
        while queue and not found:
            level_size = len(queue)
            visited_this_level = set()
            for _ in range(level_size):
                curr = queue.popleft()
                curr_dist = distance[curr]
            
                for i in range(len(curr)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == curr[i]:
                            continue
                        newWord = curr[:i] + ch + curr[i + 1 :]
                        if newWord in word_set:
                            if newWord not in distance:
                                distance[newWord] = curr_dist + 1
                                parents[newWord].add(curr)
                                visited_this_level.add(newWord)
                                if newWord == endWord:
                                    found = True
                            elif distance[newWord] == distance[curr] + 1:
                                parents[newWord].add(curr)
            for word in  visited_this_level:
                queue.append(word)
        if not found:
            return[]
        ans = []
        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()
        dfs(endWord,[endWord])        
        return ans                                    

        
 
        