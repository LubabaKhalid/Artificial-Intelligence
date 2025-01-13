from collections import Counter
def get_top_queries(search_history, topN):
    counter = Counter(search_history)
    return [(query, count) for query, count in counter.most_common(topN)]

def main():
    Hfile = "search-history.txt"
    Rfile = "search-results.txt"
    with open(Hfile, "r") as file:
        search_history = file.readlines()
    top50 = get_top_queries(search_history, 50)
    for i,j in top50:
        prob = j / len(search_history)
        #print(f'{i.strip()}  {j}     probabilty is : {prob}')
        print(f'{i.strip():<15} {j:<10} probability : {prob}')
main()