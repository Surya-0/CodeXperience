from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: 'List[str]') -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque()
        visit = set()

        queue.append((startGene, 0))
        visit.add(startGene)
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for x in 'AGCT':
                    new_gene = gene[:i] + x + gene[i + 1:]
                    if new_gene in bank and new_gene not in visit:
                        queue.append((new_gene, mutations + 1))
                        visit.add(new_gene)

        return -1

