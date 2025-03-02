import json
from tqdm import tqdm


def read_jsonl(input_file):
    with open(input_file, "r", encoding='utf-8') as f:
        lines = []
        for idx, line in enumerate(f.readlines()):
            line = json.loads(line)
            url = line["url"]
            filename = line["func_name"]
            original_code = line["code"]
            code_tokens = line["code_tokens"]
            code = " ".join(code_tokens)
            docstring_tokens = line["docstring_tokens"]
            docstring = " ".join(docstring_tokens)
            lines.append(["1", url, filename, docstring, code, original_code, ])

            if idx == 0:
                break
        return lines


input_file = r'../codesearch/python/raw_train_python.jsonl'
data = read_jsonl(input_file)

line = data[0]
print('-------this is the line-------')
print(line)
print('-------this is the line-------')
for index, i in enumerate(line):
    print(f"    {index}: {i}")
