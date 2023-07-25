from kol2testy import runtests

# Bartlomiej Szubiak
# Algorytm za pomoca algorytmu kruskala wyszukuje MST a przy okazji znajduje m (min waga) i M (max wage)
# pozniej sprawdzam czy nie wystepuja psujki czyli czy waga jakiejs krawedzi > m oraz czy < M
# wyrzucam ta krawedz chwilowo z E i uruchamiam jeszcze raz kruskala i sprawdzam czy zaszly dzrewo jest piekne
# zlononosc O(VE log* E)


class Node:
    def __init__(self,value):
        self.parent = self
        self.rank = 0
        self.value = value

def find_set(x):
    if x.parent != x :
        x.parent = find_set(x)
    return x.parent

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank :
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(edges_tab , v_no): 
    nodes = [Node(i) for i in range(v_no)]
    MST = []
    m = float('inf')
    M = 0
    for e in edges_tab:
        u,v,waga = e
        if find_set(nodes[u])!=find_set(nodes[v]):
            MST.append(e)
            union(nodes[u],nodes[v])
            M = max(M,waga)
            m = min(m,waga)
    return MST,M,m
            
        
def create_edegs_tab(G): #G[u] = (wierzcholek , waga)
    E = []
    n = len(G)
    visited_krawedzie = [[False for i in range(n)] for j in range(n)]
    for u in range(n):
        for (v , waga) in G[u]:
            if visited_krawedzie[u][v]: continue
            visited_krawedzie[u] [v] = True
            visited_krawedzie[v] [u] = True
            E.append((u,v,waga))
    return E

def find_max_waga(E,MST,m):
    for u,v,waga in reversed(E):
        if waga>m : continue
        if (u,v,waga) not in MST:
            return True #jest psujek
    return False

def find_min_waga(E,MST,M):
    for u,v,waga in E:
        if waga<M : continue
        if (u,v,waga) not in MST:
            return True #jest psujek
    return False
    

def beautree(G):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    E = create_edegs_tab(G)
    E.sort(key=lambda x : x[2])
    MST , M , m = kruskal(E,n)
    
    while find_max_waga(E,MST,m) or find_min_waga(E,MST,M): #problem z drzewem
        E_copy = E.copy()
        #wyrzucam najmniejsza krawedz z MST
        E_copy.remove(())
    
    
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = False )
# G = [ [(1,3), (2,1), (4,2)], [(0,3), (2,5) ], [(1,5), (0,1), (3,6)], [(3,4), (0,2) ] ]
# beautree(G)