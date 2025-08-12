class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        len_boxes = len(boxes)
        int_list = [c for c in boxes]
        idx_dict = {}
        for idx, e in enumerate(int_list):
            if e == '1':
                idx_dict[idx] = True
        out_list = [0] * len_boxes
        for i in range(len_boxes):
            c = boxes[i]
            total_move: int = 0
            for d_i in idx_dict.keys():
                if d_i == i:
                    pass
                else:
                    total_move += abs(d_i - i)
            out_list[i] = total_move
        #print(int_list, all_elements, idx_dict)
        return out_list

sol = Solution()
print(f'{sol.minOperations("110")} expect [1,1,3]')
print(f'{sol.minOperations("001011")} expect [11,8,5,4,3,4]')