from collections import deque
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue = deque([(startGene, 0)])   
        visited = {startGene}
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for ch in 'ACGT':
                    new_gene = gene[:i] + ch + gene[i + 1:]
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene,steps + 1))
        return -1                            
                
        