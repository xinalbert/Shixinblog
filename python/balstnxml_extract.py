'''
Author: albertxin albert_xin@qq.com
Date: 2024-07-26 10:47:04
LastEditors: albertxin albert_xin@qq.com
LastEditTime: 2024-07-26 16:04:08
FilePath: /shixinblog/python/balstnxml_extract.py
Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
'''
import sys

def parse_blast_result(file):
    '''
    ============================================================================
    parse_blast_result(file)
    ----------------------------------------------------------------------------
    解析BLASTN fmt6结果文件，找出不完全比对的序列id
    ----------------------------------------------------------------------------
    Parameters:
    file: str
        BLASTN fmt6结果文件路径
    ----------------------------------------------------------------------------
    Returns:
    ids: set
        不完全比对的序列id
    ============================================================================
    '''
    best_alignments = {}
    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            query_id = parts[0]
            bit_score = float(parts[11])
            mismatches = int(parts[4])
            gap_opens = int(parts[5])
            q_start = int(parts[6])
            q_end = int(parts[7])
            s_start = int(parts[8])
            s_end = int(parts[9])

            if query_id not in best_alignments or best_alignments[query_id]['bit_score'] < bit_score:
                best_alignments[query_id] = {
                    'bit_score': bit_score,
                    'mismatches': mismatches,
                    'gap_opens': gap_opens,
                    'q_start': q_start,
                    'q_end': q_end,
                    's_start': s_start,
                    's_end': s_end
                }

    incomplete_ids = set()
    for query_id, alignment in best_alignments.items():
        if alignment['mismatches'] + alignment['gap_opens'] != 0 or (alignment['q_start'] + alignment['q_end'] != alignment['s_start'] + alignment['s_end']):
            incomplete_ids.add(query_id)

    print(f'共找到: {len(incomplete_ids)} 条不完全比对序列！')
    return incomplete_ids

def save_file(file_path, file_content):
    with open(file_path, 'w') as f:
        for lines in file_content:
            f.write(lines + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 filter_blsatrsult.py <blastn_result_with_fmt6> <outfile>")
        sys.exit(1)
    
    file = sys.argv[1]
    # print(file)
    outfile = sys.argv[2]
    ids = parse_blast_result(file)
    save_file(outfile, ids)
