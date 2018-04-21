import re

import re

line = "Cats Cats smarter than dogs"
patterns = ["Cats than", "asu"]
ret = []
print(line)
print(patterns)

for pattern in patterns:
	pattern = pattern.split(' ')
	tmp = [-1]
	for pat in pattern:
	    matches = re.finditer(pat, line);
	    for match in matches:
	        if match.start() < tmp[len(tmp)-1]:
	        	break
	        tmp.append(match.start())
	        break;
	if len(tmp) != len(pattern)+1:
		break
	else:
		ret.append(tmp[0])
if len(ret) > 0:
    print("spam")
else:
    print("tidak spam")