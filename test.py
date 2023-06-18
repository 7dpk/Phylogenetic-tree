import re

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        if self.is_leaf():
            return self.name
        else:
            return "({}, {})".format(str(self.left), str(self.right))

def read_fasta(filename):
    with open(filename, 'r') as f:
        sequences = {}
        name = None
        sequence = ''
        for line in f:
            if line.startswith('>'):
                if name:
                    sequences[name] = sequence
                name = line.strip('>').split()[0]
                sequence = ''
            else:
                sequence += line.strip()
        sequences[name] = sequence
    return sequences

def get_ngrams(sequence, n):
    ngrams = set()
    for i in range(len(sequence)-n+1):
        ngrams.add(sequence[i:i+n])
    return ngrams

def build_tree(sequences, n):
    tree = []
    for name in sequences:
        tree.append(Node(name))
    distances = []
    for i in range(len(tree)):
        for j in range(i+1, len(tree)):
            seq1_ngrams = get_ngrams(sequences[tree[i].name], n)
            seq2_ngrams = get_ngrams(sequences[tree[j].name], n)
            jaccard = len(seq1_ngrams & seq2_ngrams) / len(seq1_ngrams | seq2_ngrams)
            distances.append((i, j, jaccard))
    distances.sort(key=lambda x: x[2], reverse=True)
    node_map = {node.name: node for node in tree}
    
    for i, j, _ in distances:
        node = Node(None)
        if str(tree[i]) < str(tree[j]):
            node.left = tree[i]
            node.right = node_map[tree[j].name]
        else:
            node.left = node_map[tree[i].name]
            node.right = tree[j]
        tree[i] = node
        tree.pop(j)
    return tree[0]
if __name__ == '__main__':
    filename = input('Enter FASTA filename: ')
    n = int(input('Enter n-gram size: '))
    sequences = read_fasta(filename)
    tree = build_tree(sequences, n)
    print(tree)