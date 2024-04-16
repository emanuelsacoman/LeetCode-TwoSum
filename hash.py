from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Função para encontrar os índices de dois números que somam o alvo.

        Args:
            nums (List[int]): Uma lista de números inteiros.
            target (int): O valor alvo que a soma dos dois números deve atingir.

        Returns:
            List[int]: Uma lista contendo os índices dos dois números que somam o alvo.

        """
        hasher = {}  # Inicializa um dicionário vazio para armazenar os valores e seus índices
        for idx, i in enumerate(nums):  # Percorre a lista de números com seus índices correspondentes
            if hasher.get(i) is not None:  # Verifica se o complemento do número atual está presente no dicionário
                return [hasher.get(i), idx]  # Se estiver presente, retorna os índices dos dois números
            hasher[target - i] = idx  # Armazena o complemento do número atual e seu índice no dicionário

# Exemplo de uso:
nums = [2, 7, 11, 15, 8, 9]
target = 10
solution = Solution()
result = solution.twoSum(nums, target)
print(result) 
"""
[0,4]
0 = 2
4 = 8

2 + 8 = target
"""
