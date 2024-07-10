# python之fasta文件统计

```python
def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def calculate_gc_content(sequences):
    all_gc = 0

    for seq in sequences:
        gc_count = seq.count('G') + seq.count('C')
        all_gc = all_gc + gc_count

    return all_gc

def calculate_n50_l50(lengths, total_length):
    sorted_lengths = sorted(lengths, reverse=True)
    cumulative_length = 0
    n50 = 0
    l50 = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= total_length * 0.5 and n50 == 0:
            n50 = length
            l50 = sorted_lengths.index(length) + 1
            break
    return n50, l50

def calculate_n90_l90(lengths, total_length):
    sorted_lengths = sorted(lengths, reverse=True)
    cumulative_length = 0
    n90 = 0
    l90 = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= total_length * 0.9 and n90 == 0:
            n90 = length
            l90 = sorted_lengths.index(length) + 1
            break
    return n90, l90

def main(fasta_file):
    sequences = read_fasta(fasta_file)
    
    num_sequences = len(sequences)
    total_length = sum(len(seq) for seq in sequences)
    gc_content = (calculate_gc_content(sequences) / total_length)*100
    
    lengths = [len(seq) for seq in sequences]
    max_length = max(lengths)
    min_length = min(lengths)
    
    n50, l50 = calculate_n50_l50(lengths, total_length)
    n90, l90 = calculate_n90_l90(lengths, total_length)
    
    print(f"total num: {num_sequences}")
    print(f"total len: {total_length}")
    print(f"GC: {gc_content:.2f}%")
    print(f"N50: {n50}")
    print(f"L50: {l50}")
    print(f"N90: {n90}")
    print(f"L90: {l90}")
    print(f"max: {max_length}")
    print(f"min: {min_length}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <fasta_file>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    main(fasta_file)
``` 

使用方法：

```
python script.py <fasta_file>    # 例如：python script.py example.fasta
``` 
输出：

```
# 示例数据，无参考意义
total num: 3
total len: 100
GC: 40.00%
N50: 50
L50: 2
N90: 90
L90: 1
max: 100
min: 50
```