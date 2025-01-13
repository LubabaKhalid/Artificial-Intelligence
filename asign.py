from collections import Counter
import time
class Node:
    def __init__(self, key, urls=None, file_reference=None):
        self.key = key
        self.urls = urls
        self.file_reference = file_reference
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert_element(self, key, urls=None, file_reference=None):
        if self.root is None:
            self.root = Node(key, urls, file_reference)
        else:
            self._insert_recursive(self.root, key, urls, file_reference)

    def _insert_recursive(self, node, key, urls, file_reference):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, urls, file_reference)
                return
            self._insert_recursive(node.left, key, urls, file_reference)
        else:
            if node.right is None:
                node.right = Node(key, urls, file_reference)
                return
            self._insert_recursive(node.right, key, urls, file_reference)

    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            if node is not None and node.urls:
                return node.urls, "memory"
            elif node is not None and node.file_reference:
                return "Read URLs from file using file_reference", "file"
            else:
                return None, None
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

def search_results_read(path):
    results = {}
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            query = parts[0]
            urls = parts[1].split(",")
            results[query] = urls
    return results

def search_history_read(path):
    with open(path, "r") as file:
        history = [line.strip() for line in file]
    return history

def get_top_queries(search_history, topN):
    counter = Counter(search_history)
    return [query for query, _ in counter.most_common(topN)]
def get_top50_queries(search_history, topN):
    counter = Counter(search_history)
    return [(query, count) for query, count in counter.most_common(topN)]
def insert(lst,n):
    if len(lst)!=0:
        mid=len(lst)//2
        
        n.insert_element(lst[mid])
        insert(lst[:mid],n)
        insert(lst[mid+1:],n)
def main():
    
    Hfile = "search-history.txt"
    Rfile = "search-results.txt"
    with open(Hfile, "r") as file:
        search_history = file.readlines()
    top50 = get_top50_queries(search_history, 50)
    for i,j in top50:
        prob = j / len(search_history)
        #print(f'{i.strip()}  {j}     probabilty is : {prob}')
        print(f'{i.strip():<15} {j:<10} probability : {prob}')
    Hfile = "search-history.txt"
    Rfile = "search-results.txt"
    topN = 10000
    
    
    history = search_history_read(Hfile)
    top_queries = get_top_queries(history, topN)
    top_queries.sort()
    bst = BinarySearchTree()
    n=BinarySearchTree()
    insert(top_queries,n)
    search_results = search_results_read(Rfile)

    for query in top_queries:
        urls = search_results.get(query, [])
        bst.insert_element(query, urls)
    
    
    
    start_time = time.time()
    user_query = input("Please enter the search query: ")
    urls, source = bst.search(user_query)
    end_time = time.time()
    execution_time=end_time-start_time
    
    
    if urls is None:
        print("Query not found.")
    else:
        print(f"Query found in {source}. URLs: {', '.join(urls)}")
        print(f"Execution time: {execution_time:.4f} seconds")
    
    

main()
