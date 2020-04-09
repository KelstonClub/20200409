# Write your code here :-)
import json
d1 = {"a" : 1, "b" : 2}
d2 = {"a" : 3, "d" : 4}

print(json.dumps(d1))
print(json.dumps(d2))

for i in range(10):
    with open("temp.json", "ab") as f:
        for d in [d1, d2]:
            f.write(json.dumps(d).encode("utf-8") + b"\n")


with open("temp.json", "rb") as f:
    for line in f:
        d = json.loads(line.strip())
