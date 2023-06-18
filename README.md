# Phylogenetic Tree

This code is designed to perform a phylogenetic analysis of DNA sequences. It parses a FASTA file containing DNA sequences, calculates the n-gram distances between them, constructs a phylogenetic tree using the neighbor joining method, and provides the option to print the tree in string format or in a more human-readable format.

## Instructions

1. Run the `phylo.py` file.
2. When prompted, enter the path of the `.fasta` file you want to analyze.
3. Enter the desired n-gram distance for calculating sequence similarity.
4. The program will generate a phylogenetic tree in string format, such as:

```
((((KF514412.1, KF514414.1), KF514416.1), (KF514417.1, KF514420.1)), (((KF514413.1, KF514423.1), KF514415.1), ((KF514418.1, KF514419.1), (KF514421.1, KF514422.1))))
```

5. If you prefer a more human-readable format, you can import the `pretty_print` function from `prettyprint.py` and pass the generated tree to the function. It will print the tree in a more visually understandable way, like this:

```
                    +--- KF514412.1
               +---|
          +---|     +--- KF514414.1
         |    |
     +---|     +--- KF514416.1
    |    |
    |    |     +--- KF514417.1
    |     +---|
    |          +--- KF514420.1
    |
    |               +--- KF514413.1
+---|          +---|
    |     +---|     +--- KF514423.1
    |    |    |
    |    |     +--- KF514415.1
    |    |
     +---|          +--- KF514418.1
         |     +---|
         |    |     +--- KF514419.1
          +---|
              |     +--- KF514421.1
               +---|
                    +--- KF514422.1
```

## TODOs

- [x] Add pretty print functionality
- [ ] Add graphical pretty print option
- [ ] Improve error handling and debugging capabilities