import networkx as nx
H = nx.DiGraph()
J = nx.DiGraph()

EGFRNodes = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/EGFR1-nodes.txt"
EGFREdges = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/EGFR1-edges.txt"
EGFRK = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/PathLinker-results/EGFR1-k_20000-ranked-edges.txt"

TGFNodes = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/TGF_beta_Receptor-nodes.txt"
TGFEdges = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/TGF_beta_Receptor-edges.txt"
TGFK = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/PathLinker-results/TGF_beta_Receptor-k_20000-ranked-edges.txt"

TNFNodes = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/TNFalpha-nodes.txt"
TNFEdges = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/TNFalpha-edges.txt"
TNFK = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/PathLinker-results/TNFalpha-k_20000-ranked-edges.txt"

WntNodes = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/Wnt-nodes.txt"
WntEdges = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/Netpath pathways/Wnt-edges.txt"
WntK = "C:/Users/nikhi/Desktop/CS 3824 Assignments/Assignment 1/PathLinker-results/Wnt-k_20000-ranked-edges.txt"

list = []

def shortestPath(nodesFile, edgesFile):    
    nodes = []
    with open(nodesFile) as nodesInFile:
        for line in nodesInFile:
            if line.split()[0] == "#node":
                continue
            if line.split()[1] == "none":
                continue
            else:
                kDict = {
                        "node" : line.split()[0], 
                        "node_type" : line.split()[1]
                        }
                H.add_node(line.split()[0])
                J.add_node(line.split()[0])
                nodes.append(kDict)
    
   
    with open(edgesFile) as edges:
        for line in edges:
            if line.split()[0] == "#tail":
                continue
            elif line.split()[5] == "physical":
                H.add_edge(line.split()[0], line.split()[1], weight = int(line.split()[2]))
                H.add_edge(line.split()[1], line.split()[0], weight = int(line.split()[2]))
            else:
                H.add_edge(line.split()[0], line.split()[1], weight = int(line.split()[2]))
    

    tfs = []
    receptors = []
    for x in nodes:
        if x.get('node_type') == "tf":
            tfs.append(x.get('node'))
        elif x.get('node_type') == "receptor":
            receptors.append(x.get('node'))

    for x in tfs:
        for y in receptors:
            try:
                path = str(nx.shortest_path(H, source=x, target=y, weight='weight', method='dijkstra'))
                path = path.replace("'", "")
                path = path.replace("[", "")
                path = path.replace("]", "")
                path = path.replace(" ", "")
                list.append(path)
            except:
                continue
    
    for x in list:
        nx.add_path(J, x.split(","))



shortestPath(WntNodes, WntEdges)
# shortestPath(TGFNodes, TGFEdges)
# shortestPath(TNFNodes, TNFEdges)
# shortestPath(EGFRNodes, EGFREdges)

print(J.edges)
