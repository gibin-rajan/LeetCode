class Solution:
    def relativeSortArray(self, arr1, arr2):
        def rank(mp, a):
            return mp.get(a, len(mp))
    
        mp = {num: i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: (rank(mp, x), x))
        return arr1