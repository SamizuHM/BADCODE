# 读入ANR-scores.txt
# 计算ANR
# 输出ANR

import numpy as np

# 路径设置为参数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--anr_scores_path','-p', type=str, default='ANR-scores.txt', help='path to ANR-scores.txt')
parser.add_argument('--total', type=int, default=1000, help='total number of queries')
args = parser.parse_args()

# 读入ANR-scores.txt
with open(args.anr_scores_path, 'r') as f:
    anr_scores = f.readlines()

# 计算ANR
anr_scores = [float(score) for score in anr_scores]
anr = np.mean(anr_scores) / args.total

# 输出ANR
print(f"ANR: {anr}")