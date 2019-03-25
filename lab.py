import sys

nodes_matrix = []
filepath = './input.txt'

def read_input():
    with open(filepath) as fp:  
       input_data = fp.readlines()
    return input_data

def find_nodes(input_data):
    node_objects = list()
    node_dict = dict()
    nodes = set()
    for line in input_data:
        node_objects.append(''.join(line).strip().replace(' ', '').split(','))
        for obj in ''.join(line).strip().replace(' ', '').split(','):
            if obj not in node_objects and obj != '':
                nodes.add(obj)
    node_count = 0
    for node in sorted(nodes):
        node_dict[node_count] = node
        node_count += 1
    print(node_dict)
        

if __name__ == '__main__':
    input_data = read_input()
    find_nodes(input_data)
