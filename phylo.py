from genome import *
from tree import *

def read_input_file(input_file):
    """Reads the input file and returns a list of Genome objects."""

    # Create an empty list to store the genomes
    genomes = []

    # Open the input file
    with open(input_file, 'r') as f:

        # Read all lines from the file
        lines = f.readlines()

        # Create an empty list to store the lines for each genome
        genome_lines = []

        # Initialize the genome name to None
        genome_name = None

        # Loop through each line in the file
        for line in lines:

            # Check if the line starts with ">"
            if line.startswith('>'):
                # If so, this is the start of a new genome

                # Check if we have lines for a previous genome
                if genome_lines:
                    # If so, create a Genome object and add it to the list
                    genome = GenomeData(genome_name, ''.join(genome_lines))
                    genomes.append(genome)

                    # Reset the genome_lines list
                    genome_lines = []

                # Set the genome name to the text after ">"
                genome_name = line.strip().lstrip('>')
                genome_name = genome_name.split()[0]
            else:
                # If the line doesn't start with ">", it's part of a genome sequence
                # Add it to the genome_lines list
                genome_lines.append(line.strip())

        # Check if there is a genome left in the genome_lines list
        if genome_name is not None:
            # If so, create a Genome object and add it to the list
            genome = GenomeData(genome_name, ''.join(genome_lines))
            genomes.append(genome)

    # Return the list of Genome objects
    return genomes


def compute_similarity(tree1, tree2):
    """Computes the similarity between two genomes using N-grams."""

    # Get the list of leaves for each tree
    list_leaves1 = tree1.get_leaves()
    list_leaves2 = tree2.get_leaves()

    # Initialize the maximum similarity to negative infinity
    max_similarity = -float('inf')

    # Loop through each pair of leaves from the two trees
    for i in list_leaves1:
        for j in list_leaves2:

            # Get the N-grams for each leaf
            ngrams1 = i.get_ngrams()
            ngrams2 = j.get_ngrams()

            # Compute the intersection and union of the N-grams
            intersection = len(ngrams1.intersection(ngrams2))
            union = len(ngrams1.union(ngrams2))

            # Compute the similarity value for this pair of leaves
            similarity = intersection / union if union != 0 else 0

            # Update the maximum similarity if necessary
            max_similarity = max(max_similarity, similarity)

    # Return the maximum similarity between any pair of leaves
    return max_similarity


def compute_phylogenetic_tree(genomes: list[GenomeData], n: int) -> Tree:
    # Create leaves for each genome
    leaves = []
    for genome in genomes:
        leaf = Tree()
        leaf._name = genome._name  # Assign genome name to tree node
        leaf._sequence = genome._sequence  # Assign genome sequence to tree node
        leaf._ngrams = genome.get_ngrams(n)  # Get n-grams of genome and assign to tree node
        leaves.append(leaf)

    # Perform hierarchical clustering
    while len(leaves) > 1:
        max_similarity = -float('inf')
        max_i = 0
        max_j = 0

        # Find the two leaves with the maximum similarity
        for i in range(len(leaves)):
            for j in range(len(leaves)):
                # Check if we are not comparing the same objects
                if i != j:
                    similarity = compute_similarity(leaves[i], leaves[j])  # Compute similarity between two nodes
                    if similarity > max_similarity:
                        max_similarity = similarity
                        max_i = i
                        max_j = j

        # Merge the two leaves into a new node
        merged_tree = Tree()

        """Set children of non-leaf node as follows:
          if t1._name < t2._name, t1 is left child, otherwise t2 is left child."""
        if leaves[max_i]._name < leaves[max_j]._name:
            merged_tree._left = leaves[max_i]
            merged_tree._right = leaves[max_j]
            tree1_name = leaves[max_i]._name
            tree2_name = leaves[max_j]._name
            merged_tree._name = f"({tree1_name},{tree2_name})"
        else:
            merged_tree._left = leaves[max_j]
            merged_tree._right = leaves[max_i]
            tree1_name = leaves[max_j]._name
            tree2_name = leaves[max_i]._name
            merged_tree._name = f"({tree1_name},{tree2_name})"


        # Update the list of leaves
        if max_i < max_j:
            leaves.pop(max_j)
            leaves.pop(max_i)
        else:
            leaves.pop(max_i)
            leaves.pop(max_j)
        leaves.append(merged_tree)

    return leaves[0]

def print_phylogenetic_tree(tree: Tree) -> None:
    """Prints the phylogenetic tree without indentation."""
    if tree is None:
        return

    if tree.is_leaf():
        print(tree._name, end='')  # Print leaf name without whitespace
        return

    print('(', end='')
    print_phylogenetic_tree(tree._left)  # Recursively print left subtree
    print(',', end=' ')
    print_phylogenetic_tree(tree._right)  # Recursively print right subtree
    print(')', end='')

if __name__ == '__main__':
    # Get input file and n-gram size from user
    input_file = input('FASTA file: ')
    n = int(input('n-gram size: '))

    # Read genomes from input file
    genomes = read_input_file(input_file)

    # Compute phylogenetic tree
    tree = compute_phylogenetic_tree(genomes, n)
    
    # Print phylogenetic tree
    print_phylogenetic_tree(tree)