import sys
  
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
    for node in sorted(nodes, key=lambda x: int(x.split('-')[0]*100) + int(x.split('-')[1])):
        node_dict[node] = node_count
        node_count += 1
    return node_objects, node_dict

def create_matrix(node_objects, node_dict):
  matrix = [[0 for x in range(len(node_dict))] for y in range(len(node_dict))] 
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
  phis = []
  for row_idx in range(0, len(node_matrix)):
    cur_row = node_matrix[row_idx]
    cur_row_number = int(get_row_number(cur_row), 2) # print(cur_row_number)# TODO: watch overflow ?
    row_zero_values = get_row_zero_values(cur_row, row_idx) # print(row_zero_values)
    concat_value = cur_row_number
    cur_phi = [row_idx]
    for zero_row in row_zero_values:
          zero_row_value = int(get_row_number(node_matrix[zero_row]), 2)
          if concat_value | zero_row_value > concat_value:
            concat_value = concat_value | zero_row_value
            cur_phi.append(zero_row)
          if concat_value == int(len(node_matrix) * ('1'), 2):
            phis.append(cur_phi)
            break
  return phis

def get_row_number(cur_row):
    return ''.join(str(x) for x in cur_row)

def get_row_zero_values(cur_row, row_idx):
    zeroes = []
    for idx in range(row_idx, len(cur_row)):
      if cur_row[idx] == 0:
        zeroes.append(idx)
    return zeroes

def get_phis_nodes(phis, node_dict):
  phi_names = []
  for node_row in phis:
    cur_phi_row = []
    for node in node_row:
      node_name = next((val for val, cnt in node_dict.items() if cnt == node), None)
      cur_phi_row.append(node_name)
    phi_names.append(cur_phi_row)
  return phi_names

def create_alpha_matrix(phis):
  alpha_matrix = [[0 for x in range(len(phis))] for y in range(len(phis))]
  for row_idx1 in range(0, len(phis)):
    phi_row1 = phis[row_idx1]
    for row_idx2 in range(row_idx1 + 1, len(phis)):
      phi_row2 = phis[row_idx2]
      cur_alpha = len(phi_row1) + len(phi_row2) - len(list(set(phi_row1) & set(phi_row2)))
      alpha_matrix[row_idx1][row_idx2] = cur_alpha
      alpha_matrix[row_idx2][row_idx1] = cur_alpha
  return alpha_matrix

if __name__ == '__main__':
    input_data = read_input()
    node_objects, node_dict = find_nodes(input_data)
    node_matrix = create_matrix(node_objects, node_dict)
    print('Renamed matrix:\n', node_dict)
    for i in range(0, len(node_dict)):
      print(node_matrix[i])
    phis = build_phis(node_matrix)
    print('\nPhis:\n', phis)
    phi_names = get_phis_nodes(phis, node_dict)
    print('\nPhis with names:')
    for phi in phi_names:
        print(phi)
    alpha_matrix = create_alpha_matrix(phis)
    print('\nAlpha matrix:')
    for alpha in alpha_matrix:
        print(alpha)