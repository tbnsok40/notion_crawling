from collections import defaultdict
from private_data import *

interviewer = [park, cha, lim, lee, seo]

final_dict = defaultdict(float)
final_result = defaultdict(float)
for j in interviewer:
    if len(j) == 28:
        for i in j:
            a, b = i.split(' ')
            b = float(b)
            final_dict[a] += b
    else:
        print(False)
        break

for i in final_dict.items():
    final_result[i[0]] = i[1] / len(interviewer)

sorted_Final = sorted(final_result.items(), key=lambda x: x[1], reverse=True)
for i, final in enumerate(sorted_Final):
    if i == 15:
        print('-------------')

    print(final[0], round(final[1], 3))
