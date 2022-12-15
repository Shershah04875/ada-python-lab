class a_matrix:
    def __init__(self, v):
        self.v=v
        self.matrix=[[0 for i in range(v)] for i in range(v)]         #if matrix of n*n siz4


    def add_edge(self,v1,v2):
        if (v1==v2):
            return
        self.matrix[v1][v2]=1
        self.matrix[v2][v1]=1
        
    def remove(self, v1, v2):
        if self.matrix[v1][v2] > 0:
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
        
    def print_matrix(self):
        for row in self.matrix:
            print(row)
        print("\n")


v = int(input("No of vertices: "))
# Grapgh initialization
m=a_matrix(v)

# Rows as input
for i in range(v):
    row = input(f"Enter row {i}: ").split(" ")
    # convert into list of integers
    row = [int(item) for item in row]
    for i in range(len(row)):
        if row[i]!= 0:
            m.add_edge(1,i)

m.print_matrix()
