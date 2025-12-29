class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        allowed_set = defaultdict(list)

        for ch in allowed:
            allowed_set[ch[:2]].append(ch[2])
        
        def rec(bottom2):
            if len(bottom2) == 2 and bottom2 in allowed_set:
                return True
            
            layer_list = []
            for i in range(len(bottom2) - 1):
                curr = bottom2[i:i+2]
                temp = []
                if curr in allowed_set:
                    if not layer_list:
                        for ch in allowed_set[curr]:
                            temp.append(ch)
                    else:
                        for layer in layer_list:
                            for ch in allowed_set[curr]:
                                temp.append(layer + ch)
                else:
                    return False

                layer_list = temp

            return any(rec(ch) for ch in layer_list)                

        return rec(bottom)