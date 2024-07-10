# 准备一个Python脚本统计fastq文件的序列条数、碱基总数、Q20占比、Q30占比

```python
import gzip

def count_fastq_stats(file_path):
    total_seq_nu = 0
    total_base_nu = 0
    q20_count = 0
    q30_count = 0

    def is_gzipped(file_path):
        with open(file_path, 'rb') as f:
            return f.read(2) == b'\x1f\x8b'

    open_func = gzip.open if is_gzipped(file_path) else open

    with open_func(file_path, 'rt') as f:
        while True:
            # Read four lines at a time (one sequence)
            lines = [f.readline() for _ in range(4)]
            if not lines[0]:
                break  # End of file

            total_seq_nu += 1
            sequence = lines[1].strip()
            total_base_nu += len(sequence)
            qualities = lines[3].strip()

            for qual in qualities:
                qual_score = ord(qual) - 33  # Convert ASCII to quality score
                if qual_score >= 20:
                    q20_count += 1
                if qual_score >= 30:
                    q30_count += 1

    q20_percentage = (q20_count / total_base_nu) * 100 if total_base_nu else 0
    q30_percentage = (q30_count / total_base_nu) * 100 if total_base_nu else 0

    print(f"total seq nu: {total_seq_nu}")
    print(f"total base nu: {total_base_nu}")
    print(f"Q20: {q20_percentage:.2f}%")
    print(f"Q30: {q30_percentage:.2f}%")



if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <fastq_file>")
        sys.exit(1)
    
    fastq_file = sys.argv[1]
    count_fastq_stats(fastq_file)
```

这个脚本能够用于统计fastq文件的序列条数、碱基总数、Q20占比、Q30占比。
文件输入支持fastq和gzip压缩格式。

使用方法：

```
python script.py <fastq_file>
```

