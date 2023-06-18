class GenomeData:
    def __init__(self, name, sequence):
        self._name = name
        self._sequence = sequence
        self._ngrams = set()
    
    def get_name(self):
        return self._name
    def get_sequence(self):
        return self._sequence
    
    def get_ngrams(self, N):
        """Constructs the set of n-grams for the genome."""
        return set([self._sequence[i: i + N] for i in range(len(self._sequence) - N + 1)])


