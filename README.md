# huffman-coding

Simple program that uses a Huffman algorithm to encode strings and text files.

## Pseudocode

### Huffman

```python
procedure Huffman(f)
Input: An array f[1···n] of frequencies
Output: An encoding tree with n leaves

let H be a priority queue of integers, ordered by f
for i = 1 to n: insert(H,i)
for k = n + 1 to 2n − 1:
    i = deletemin(H), j = deletemin(H)
    create a node numbered k with children i,j
    f[k] = f[i] + f[j]
    insert(H,k)
```

## Running the tests

### Inputs

Input 1: (just a string):

```
missisipi
```

Input 2: [text file](snark.txt)

### Outputs

The output table is formatted as:

Character | Frequency of that character | Huffman code corresponding to that character

For Input 1:
```

```

For Input 2:
```

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Algorithms - S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
