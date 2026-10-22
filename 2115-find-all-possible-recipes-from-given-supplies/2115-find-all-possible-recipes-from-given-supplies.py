from collections import deque
from collections import defaultdict
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(recipes)):
            recipe = recipes[i]
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)
        queue = deque(supplies)
        answer = []
        while queue:
            node = queue.popleft()
            for recipe in graph[node]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    answer.append(recipe)
                    queue.append(recipe)

        return answer            

        