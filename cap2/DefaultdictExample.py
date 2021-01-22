d = {}
d['age'] = d.get('age',0) + 1
print(d)

d = {'age':39}
d['age'] = d.get('age',0) + 1
print(d)

from collections import defaultdict
dd = defaultdict(int)
dd['age'] += 1
print(dd)