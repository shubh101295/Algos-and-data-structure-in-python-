# solution to codeforces edu 
# segment trees step 1 part 1 practise q1 
# passes the tests because the timings for each language was appropriately scaled

class SegTree():
    def __init__(self , n):
        self.size = 1
        self.nn =n-1
        while self.size<n:
            self.size*=2
        self.sums = [0]*(2*self.size)
        # print(f"self.size == {self.size}")
        
    def build_2(self,v,x, lx,rx):
        if rx-lx==1:
            if lx<self.nn:
                # print(lx, rx ,"AB")
                self.sums[x]=v[lx]
                # print(self.sums)
            return
        mid = (lx+rx)//2 
        # print(x, lx,rx )
        self.build_2(v,2*x+1 , lx,mid)
        self.build_2(v,2*x+2 , mid,rx)
        self.sums[x] = self.sums[2*x+1] + self.sums[2*x+2]
    
    def build(self,v):
        # print("1")
        self.build_2(v, 0,0,self.size)  
    
    def set_2(self, i,y, x, lx,rx):
        if rx-lx==1:
            self.sums[x] = y 
            return
        mid =  (lx+rx)//2 
        if i< mid:
            self.set_2(i,y,2*x+1 , lx,mid)
        else:
            self.set_2(i,y,2*x+2 , mid,rx)
        self.sums[x] = self.sums[2*x+1] + self.sums[2*x+2]

    def set(self,i,y):
        self.set_2(i,y,0,0,self.size)

    def get_sum_2(self,l,r,x,lx,rx):
        # print(l,r,x,lx,rx)
        if l<=lx and rx<=r:
            return self.sums[x] 
        if rx<=l or r<=lx:
            return 0
        mid = (lx+rx)//2
        s1 = self.get_sum_2(l,r,2*x+1, lx,mid)
        s2 = self.get_sum_2(l,r,2*x+2 ,mid ,rx)
        return s1+s2
        
    
    def get_sum(self,l,r):
        return self.get_sum_2(l,r,0,0,self.size)
    
    def print_Tree(self):
        print(self.sums)
    

n,m = list(map(int,input().strip().split()))[0:2]

v = list(map(int,input().strip().split()))[0:n]

st = SegTree(n+1)
st.build(v)

# st.print_Tree()


i=0
while i<m:
    i+=1
    x,l,r = list(map(int,input().strip().split()))[0:3]
    # print(l,r)
    if x==2:
        print(st.get_sum(l,r))
    else:
        st.set(l,r)
