
class DSU:
    def __init__(self,n):
        self.parent = [0]*n
        for i in range(n):
            self.parent[i]=i
        self.size = n
    
    def find_set(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]
    
    def union_set(self,a,b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a!=b:
            self.parent[a]=b 
    
    def find_parent_all(self):
        for i in range(self.size):
            self.parent[i] = self.find_set(i)
