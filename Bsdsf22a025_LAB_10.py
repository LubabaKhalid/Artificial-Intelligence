import math
import random

# Calculate entropy of a dataset
def calculate_entropy(data, target_col):
    total_count = len(data)
    value_counts = {}
    
    for row in data:
        label = row[target_col]
        if label not in value_counts:
            value_counts[label] = 0
        value_counts[label] += 1
    
    entropy = 0
    for label in value_counts:
        prob = value_counts[label] / total_count
        entropy -= prob * math.log2(prob)
    
    return entropy

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    attribute_values = set([row[attribute] for row in data])
    weighted_entropy = 0
    for value in attribute_values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy

def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if len(set([row[target_col] for row in data])) == 1:
        return data[0][target_col]
    if depth >= max_depth:
        return max(set([row[target_col] for row in data]), key=[row[target_col] for row in data].count)
    best_attribute = None
    best_info_gain = 0
    for attribute in attributes:
        info_gain = calculate_information_gain(data, attribute, target_col)
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_attribute = attribute
    tree = {best_attribute: {}}
    attribute_values = set([row[best_attribute] for row in data])
    for value in attribute_values:
        subset = [row for row in data if row[best_attribute] == value]
        tree[best_attribute][value] = build_tree(subset, [a for a in attributes if a != best_attribute], target_col, depth + 1, max_depth)
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):  
        return tree
    root_attribute = list(tree.keys())[0]
    attribute_value = data_point[root_attribute]
    return predict(tree[root_attribute][attribute_value], data_point)

def build_random_forest(data, attributes, target_col, n_trees=2):
    trees = []
    for _ in range(n_trees):
        sampled_data = random.choices(data, k=len(data))
        tree = build_tree(sampled_data, attributes, target_col)
        trees.append(tree)
    return trees

def random_forest_predict(forest, data_point):
    predictions = [predict(tree, data_point) for tree in forest]
    return max(set(predictions), key=predictions.count)

def main():
    dataset = [
        {"Weather": "Sunny", "Temperature": "Hot", "Play?": "No"},
        {"Weather": "Overcast", "Temperature": "Hot", "Play?": "Yes"},
        {"Weather": "Rainy", "Temperature": "Mild", "Play?": "Yes"},
        {"Weather": "Sunny", "Temperature": "Mild", "Play?": "No"},
        {"Weather": "Overcast", "Temperature": "Mild", "Play?": "Yes"},
        {"Weather": "Rainy", "Temperature": "Hot", "Play?": "No"}
    ]
    
    attributes = ["Weather", "Temperature"]
    target_col = "Play?"
    entropy = calculate_entropy(dataset, target_col)
    print(f"Entropy of the entire dataset: {entropy}")
    for attribute in attributes:
        info_gain = calculate_information_gain(dataset, attribute, target_col)
        print(f"Information Gain for {attribute}: {info_gain}")
    forest = build_random_forest(dataset, attributes, target_col, n_trees=2)
    print("Random Forest model built with 2 trees.")
    new_data_points = [
        {"Weather": "Sunny", "Temperature": "Hot"},
        {"Weather": "Rainy", "Temperature": "Mild"},
        {"Weather": "Overcast", "Temperature": "Hot"}
    ]
    for data_point in new_data_points:
        prediction = random_forest_predict(forest, data_point)
        print(f"Prediction for {data_point}: {prediction}")
if __name__ == "__main__":
    main()
