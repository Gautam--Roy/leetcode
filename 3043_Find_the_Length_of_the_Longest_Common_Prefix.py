ass Solution:
        def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
            mapPref = {}
                               for num in arr1:
                str_num = str(num)
                prefix = ""
                for ch in str_num:
                        prefix += ch
                        mapPref[prefix] = mapPref.get(prefix, 0) + 1
                
                max_length = 0
            for num in arr2:
                str_num = str(num)
                prefix = ""
                for ch in str_num:
                        prefix += ch
                        if prefix in mapPref:
                                max_length = max(max_length, len(prefix))
                    return max_length
