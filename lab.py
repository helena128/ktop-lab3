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
        node_objects.append(list(filter(None, ''.join(line).strip().replace(' ', '').split(','))))
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
	#print(len(matrix[0]))
	for main_node in node_objects:
		main_node_idx = int(node_dict.get(main_node[0]))
		for node in main_node:
			if main_node == node: continue
			suppl_node_idx = node_dict.get(node)
			matrix[main_node_idx][suppl_node_idx] = 1
			matrix[suppl_node_idx][main_node_idx] = 1
	for i in range(0, len(node_dict)):
		for j in range(0, len(node_dict)):
			if i == j:
				matrix[i][j] = 1
	return matrix

def build_phis(node_marix):
	for row_idx in range(0, len(node_matrix)):
		cur_row = node_matrix[row_idx]
		cur_row_number = int(get_row_number(cur_row), 2)# print(cur_row_number)# TODO: watch overflow ?
		row_zero_values = get_row_zero_values(cur_row)# print(row_zero_values)
		last_row = 0
		for zero_var in row_zero_values:
   	 		print(zero_var)
	return []

def get_row_number(cur_row):
    return ''.join(str(x) for x in cur_row)

def get_row_zero_values(cur_row):
    zeroes = []
    for idx in range(0, len(cur_row)):
    	if cur_row[idx] == 0:
    		zeroes.append(idx)
    return zeroes

if __name__ == '__main__':
    input_data = read_input()
    node_objects, node_dict = find_nodes(input_data)
    #print(node_objects)
    #print(node_dict)
    node_matrix = create_matrix(node_objects, node_dict)
    for i in range(0, len(node_objects)):
    	print(node_matrix[i])
    phis = build_phis(node_matrix)