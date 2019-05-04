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
    cur_row_number = int(get_row_number(cur_row), 2) # base row value as int
    row_zero_values = get_row_zero_values(cur_row, row_idx) # 
    concat_value = cur_row_number
    cur_phi = [row_idx]
    #print('\n\nBase row: ', row_idx, ' Zeroes in positions: ', row_zero_values)
    if concat_value == int(len(node_matrix) * ('1'), 2):
      phis.append(cur_phi)
    for zero_row_idx in range(0, len(row_zero_values)):
      found_phi = find_phis_in_array(cur_row_number, node_matrix, row_zero_values[zero_row_idx:])
      if found_phi != None:
        #print('> Found: ', found_phi)
        phis.append([row_idx] + found_phi)
  return phis

def find_phis_in_array(cur_value, node_matrix, zero_row_values):
  print('Zero array: ' , zero_row_values)
  concat_value = cur_value
  cur_phi = []
  for row in zero_row_values:
    zero_row_value = int(get_row_number(node_matrix[row]), 2)
    if concat_value | zero_row_value > concat_value:
      concat_value = concat_value | zero_row_value
      cur_phi.append(row)
  return cur_phi if concat_value == int(len(node_matrix) * ('1'), 2) else None

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

def minimize_alphas(alphas, phis):
  phi1, phi2, max_intersection = find_max(alphas)
  if max_intersection == 0:
    print('Finished')
    return
  new_phis = rebuild_phis(phis, phi1, phi2)
  print('Rebuild phis: ', new_phis)

def rebuild_phis(phis, phi1, phi2):
  new_phis = dict()
  phi1_row = phis[phi1]
  phi2_row = phis[phi2]
  for i in range (0, len(phis)):
    if i == phi1 or i == phi2:
      continue
    cur_phi_row = []
    for j in range (0, len(phis[i])):
      if phis[i][j] not in phi1_row and phis[i][j] not in phi2_row:
        cur_phi_row.append(phis[i][j])
    new_phis[i] = cur_phi_row
  return new_phis

def find_max(alphas):
  #if not isinstance(alphas, dict):
  max_intersection = 0
  phi1 = 0
  phi2 = 0
  for i in range(0, len(alphas)):
    for j in range(i + 1, len(alphas)):
      if alphas[i][j] > max_intersection:
        max_intersection = alphas[i][j]
        phi1 = i
        phi2 = j
  print('Max intersection: ', max_intersection, ' Phis: ', phi1, ' ', phi2)
  return phi1, phi2, max_intersection

def rebuild_alpha_matrix(phis):
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
    minimize_alphas(alpha_matrix, phi_names)