# 2213. Longest Substring of One Repeating Character
# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        '''
        # TLE
        def findmaxlen(s):
            prev=s[0]
            i=1
            count=1
            ans=0
            while i<len(s):
                if s[i]==prev:
                    count+=1
                else:
                    ans=max(ans,count)
                    prev=s[i]
                    count=1
                i+=1
            ans=max(ans,count)
            return ans
        ans=[]
        s=list(s)
        for i in range(len(queryIndices)):
            s[queryIndices[i]]=queryCharacters[i]
            ans.append(findmaxlen("".join(s)))
        return ans
        '''

'''
# Ref: https://leetcode.com/problems/longest-substring-of-one-repeating-character/discuss/1866248/Python-Segment-Tree-(a-version-which-won't-get-TLE)
class SegmentTree:
    def __init__(self, data):
        self.nodes = [None] * 4 * len(data) #node: (value, left_node_index, right_node_index)
        self.data = data
        self._build_tree(0, 0, len(data)-1)

    def _left(self, index):
        return (index + 1) * 2 - 1

    def _right(self, index):
        return (index + 1) * 2

    def _build_tree(self, node_index, left_data_index, right_data_index):
        value = None
        if left_data_index == right_data_index:
            # (longest c, longest len, prefix c, prefix len, suffix c, suffix len)
            value = (
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1,
                self.data[left_data_index],
                1)
        else:
            left_node_index = self._left(node_index)
            right_node_index = self._right(node_index)

            mid_data_index = (left_data_index + right_data_index) // 2
            (left_lc, left_ll, left_pc, left_pl, left_sc, left_sl) = self._build_tree(left_node_index, left_data_index, mid_data_index)
            (right_lc, right_ll, right_pc, right_pl, right_sc, right_sl) = self._build_tree(right_node_index, mid_data_index + 1, right_data_index)
            
            lc = ll = None
            if left_ll > right_ll:
                lc = left_lc
                ll = left_ll
            else:
                lc = right_lc
                ll = right_ll
            if left_sc == right_pc and left_sl + right_pl > ll:
                ll = left_sl + right_pl
                lc = left_sc

            pc = left_pc
            pl = left_pl
            if left_pl == (mid_data_index - left_data_index + 1) and left_pc == right_pc:
                pl = left_pl + right_pl

            sc = right_sc
            sl = right_sl
            if right_sl == (right_data_index - mid_data_index) and left_sc == right_sc:
                sl = left_sl + right_sl
    
            value = (lc, ll, pc, pl, sc, sl)

        self.nodes[node_index] = value
        return value

    def _update(self, node_index, data_index, update_value, left_data_index, right_data_index):
        value = self.nodes[node_index]
        mid_data_index = (left_data_index + right_data_index) // 2
        left_node_index = self._left(node_index)
        right_node_index = self._right(node_index)

        new_value = None
        if left_data_index == right_data_index:
            new_value = (
                update_value,
                1,
                update_value,
                1,
                update_value,
                1)
        else:
            left_value = right_value = None
            if data_index <= mid_data_index:
                left_value = self._update(left_node_index, data_index, update_value, left_data_index, mid_data_index)
                right_value = self.nodes[right_node_index]
            else:
                left_value = self.nodes[left_node_index]
                right_value = self._update(right_node_index, data_index, update_value, mid_data_index + 1, right_data_index)
            (left_lc, left_ll, left_pc, left_pl, left_sc, left_sl) = left_value
            (right_lc, right_ll, right_pc, right_pl, right_sc, right_sl) = right_value
            
            lc = ll = None
            if left_ll > right_ll:
                lc = left_lc
                ll = left_ll
            else:
                lc = right_lc
                ll = right_ll
            if left_sc == right_pc and left_sl + right_pl > ll:
                ll = left_sl + right_pl
                lc = left_sc

            pc = left_pc
            pl = left_pl
            if left_pl == (mid_data_index - left_data_index + 1) and left_pc == right_pc:
                pl = left_pl + right_pl

            sc = right_sc
            sl = right_sl
            if right_sl == (right_data_index - mid_data_index) and left_sc == right_sc:
                sl = left_sl + right_sl
    
            new_value = (lc, ll, pc, pl, sc, sl)
        self.nodes[node_index] = new_value
        return new_value

    def update(self, data_index, update_value):
        self.data[data_index] = update_value
        return self._update(0, data_index, update_value, 0, len(self.data)-1)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(list(s))
        M = len(queryCharacters)
        ans = [0] * M
        for i in range(M):
            c = queryCharacters[i]
            p = queryIndices[i]
            st.update(p, c)
            ans[i] = st.nodes[0][1]
        return ans        
'''