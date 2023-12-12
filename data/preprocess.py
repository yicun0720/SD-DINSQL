import json

data = []

# 将数据写入 JSON 文件
with open("tpcds/dev.json", "w") as json_file:
    with open('tpcds/dev_data', 'r') as f:
        s = f.read()
        s = s.split('\n')
        for line in s:
            data.append({"db_id": "tpcds", "question": line})
    json.dump(data, json_file)