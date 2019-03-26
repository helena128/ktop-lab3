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
    for node in sorted(nodes, key=lambda x: int(x.split('-')[0])):
        node_dict[node] = node_count
        node_count += 1
    return node_objects, node_dict
    

def create_matrix(node_objects, node_dict):
	matrix = [[0 for x in range(len(node_dict))] for y in range(len(node_dict))] 
	print(len(matrix[0]))
	for node_idx in range(0, len(node_objects)):
		main_node_idx = node_dict.get(node_objects[node_idx][0])
		#print(node_objects[node_idx][0], main_node_idx)
		#print(node_objects)
		print(node_objects[main_node_idx])
		for i in range(1, len(node_objects[main_node_idx])): 
			print(i)
			#print(i, node_dict.get(node_objects[node_idx][i]))
			#suppl_node_idx = int(node_dict.get(node_objects[node_idx][i]))	
			#matrix[main_node_idx][suppl_node_idx] = 1
			#matrix[suppl_node_idx][main_node_idx] = 1
	for i in range(0, len(node_dict)):
		for j in range(0, len(node_dict)):
			if i == j:
				matrix[i][j] = 1
	return matrix


if __name__ == '__main__':
    input_data = read_input()
    node_objects, node_dict = find_nodes(input_data)
    #print(node_objects)
    #print(node_dict)
    node_marix = create_matrix(node_objects, node_dict)
    for i in range(0, len(node_objects)):
    	print(matrix[i])