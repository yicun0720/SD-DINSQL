import json

CODEX = []
with open('debug_sqls0.json', 'r') as f:
    sqls_0 = json.load(f)

with open('debug_sqls1.json', 'r') as f:
    sqls_1 = json.load(f)

for i in range(0, len(sqls_0)):
    sql = sqls_0[i]
    sql["debug_answers2"] = sqls_1[i]["debug_answers1"]
    CODEX.append(sql)

with open('debug_sqls.json', 'w') as out:
    json.dump(CODEX, out)


