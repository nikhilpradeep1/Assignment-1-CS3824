import matplotlib.pyplot as plt
import networkx as nx

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


def storeNodes(nodeFile):
    #store nodes in list of dicts
    nodes = []
    with open(nodeFile) as nodesInFile:
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
                nodes.append(kDict)
    return nodes

#create graph of edges for -edges.txt file
def graphEdges(edgeFile):
    H = nx.DiGraph()
    with open(edgeFile) as edges:
        for line in edges:
            if line.split()[0] == "#tail":
                continue
            elif line.split()[5] == "physical":
                H.add_edge(line.split()[0], line.split()[1], weight = line.split()[2])
                H.add_edge(line.split()[1], line.split()[0], weight = line.split()[2])
            else:
                H.add_edge(line.split()[0], line.split()[1], weight = line.split()[2])
    return H

#store k_20000 edges in list of dicts
def storeK20000(kFile):
    k2rankedEdges = []
    total = 0.0
    with open(kFile) as edges:
        for line in edges:
            if line.split()[0] == "#tail":
                continue
            else:
                total = total + 1;
                kDict = {
                        "tail" : line.split()[0], 
                        "head" : line.split()[1], 
                        "ksp" : line.split()[2]
                        }
                k2rankedEdges.append(kDict)
    return k2rankedEdges

def getTotal(kFile):
    total = 0.0
    with open(kFile) as edges:
        for line in edges:
            if line.split()[0] == "#tail":
                continue
            else:
                total = total + 1;
    return total

def precRec(H, k20000, total, name):
#calculate precision and recall
    precision = []
    recall = []
    trueP = 0.0;
    rank = 0.0;
    for x in k20000:
        try:
            H[x.get('tail')][x.get('head')]
            trueP = trueP + 1
            rank = float(x.get('ksp'))
            precision.append(trueP/rank)
            recall.append(trueP/total)
        except:
            rank = float(x.get('ksp'))
            precision.append(trueP/rank)
            recall.append(trueP/total)

    yA = precision
    xA = recall

    plt.plot(xA, yA, label=name)
    plt.legend()



storeNodes(WntNodes)
precRec(graphEdges(WntEdges), storeK20000(WntK), getTotal(WntK), "Wnt")
storeNodes(EGFRNodes)
precRec(graphEdges(EGFREdges), storeK20000(EGFRK), getTotal(EGFRK), "EGFR")
storeNodes(TGFNodes)
precRec(graphEdges(TGFEdges), storeK20000(TGFK), getTotal(TGFK), "TGF")
storeNodes(TNFNodes)
precRec(graphEdges(TNFEdges), storeK20000(TNFK), getTotal(TNFK), "TNF")

plt.show()


