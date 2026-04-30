class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # 2. Преобразуем словарь в список кортежей и сортируем по убыванию частоты
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # 3. Возвращаем только первые k элементов
        return [item for item, _ in sorted_items[:k]]
