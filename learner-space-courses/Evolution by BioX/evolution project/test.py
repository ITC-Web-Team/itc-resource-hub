from Bio import SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
import pylab

def read_fasta(file_path):
    """Read sequences from a FASTA file and return a MultipleSeqAlignment object."""
    records = list(SeqIO.parse(file_path, "fasta"))
    alignment = MultipleSeqAlignment(records)
    return alignment

# File path to your FASTA file
fasta_file = "sequences.fasta"  # Replace with your file path

# Read sequences from FASTA file
alignment = read_fasta(fasta_file)

# Calculate genetic distance matrix
calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)
print("Distance Matrix:")
print(distance_matrix)

# Construct phylogenetic tree using UPGMA
constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)

# Print ASCII representation of the tree
print("\nPhylogenetic Tree (ASCII):")
Phylo.draw_ascii(tree)

# Draw and show the phylogenetic tree using pylab
print("\nDisplaying graphical phylogenetic tree using pylab...")
Phylo.draw(tree)
pylab.show()
