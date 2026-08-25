class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        n=len(temperatures)
        r=[0]*n
        for i,t in enumerate(temperatures):
            while st and t>st[-1][0]:
                warmer, idx=st.pop()
                r[idx]= i-idx
            st.append((t,i))
        return r



        