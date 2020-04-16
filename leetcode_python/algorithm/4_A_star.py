tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}

tree2 = {'S': [['A', 1], ['B', 2]],
         'A': [['S', 1]],
         'B': [['S', 2], ['C', 3], ['D', 4]],
         'C': [['B', 2], ['E', 5], ['F', 6]],
         'D': [['B', 4], ['G', 7]],
         'E': [['C', 5]],
         'F': [['C', 6]]
         }

heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}
heuristic2 = {'S': 0, 'A': 5000, 'B': 2, 'C': 3, 'D': 4, 'E': 5000, 'F': 5000, 'G': 0}

cost = {'S': 0}


def AStarSearch():
    global tree, heuristic
    closed, opened = [], [['S', 8]]

    # 找到访问过的结点
    while True:
        fn = [i[1] for i in opened]     # 找出所有的启发值
        chosen_index = fn.index(min(fn))    # 选择最小的启发值
        node = opened[chosen_index][0]      # 匹配对应的结点
        closed.append(opened[chosen_index])

        del opened[chosen_index]   # 防止一直选择同样的最小值

        if closed[-1][0] == 'G':
            break

        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue

            # 计算启发值
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]

            temp = [item[0], fn_node]
            opened.append(temp)

    # 找到最优序列
    trace_node = "G"  # 从目标结点开始反向查找
    optimial_sequance = ['G']
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimial_sequance.append(check_node)
                trace_node = check_node

    optimial_sequance.reverse()
    return closed, optimial_sequance

if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))