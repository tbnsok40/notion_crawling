from collections import defaultdict
from private_data import park, cha, lim, lee, seo

# interviewer 리스트의 각 element 는 ['이름 점수', '이름 점수', ...] 형태의 리스트 자료형.
interviewer = [park, cha, lim, lee, seo]
final_result = defaultdict(float)

for j in interviewer:
    if len(j) == 28:
        for i in j:
            a, b = i.split(' ')
            final_result[a] += float(b)
    else:
        print(False)
        break

for i in final_result.items():
    final_result[i[0]] = i[1] / len(interviewer)

# 최고점부터 내림차순 정렬
sorted_Final = sorted(final_result.items(), key=lambda x: x[1], reverse=True)

for i, final in enumerate(sorted_Final):
    # 15명 커트
    if i == 15:
        print('-------------')
    print(final[0], round(final[1], 3))
