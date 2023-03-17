def find_medals(scores):
    sorted_scores = sorted([i for i in enumerate(scores)], key=lambda x: x[1], reverse=True)
    medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
    for i in range(len(sorted_scores)):
        if medals:
            scores[sorted_scores[i][0]] = medals.pop(0)
        else:
            scores[sorted_scores[i][0]] = str(i + 1)
    return scores  

find_medals([10,3,8,9,4])