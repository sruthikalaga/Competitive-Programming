import unittest

def bfs_search_to_path(graph, start, end):

    start_node = graph.setdefault(start, None)
    end_node = graph.setdefault(end, None)
    if(start_node == None or end_node == None):
        raise Exception
    visit_made = []
    parent_list = {}
    queue_of_nodes = []
    flag = False
    queue_of_nodes.append(start)
    while(len(queue_of_nodes)>0 and flag == False):
        node = queue_of_nodes.pop(0)
        if(node not in visit_made):
            visit_made.append(node)
            temp_node = graph[node]
            for x in temp_node:
                if (x!=end and x not in visit_made):
                    parent_list[x]=node
                    queue_of_nodes.append(x)
                elif(x==end):
                    queue_of_nodes.append(x)
                    parent_list[x]=node
                    flag = True
                    break
    var1 = parent_list.setdefault(end,None)
    
    if (var1 == None):
        return None
    else:
        result = []
        curr = end
        while(curr != start):
            result.append(curr)
            curr = parent_list[curr]
        result.append(curr)
        result.reverse()
        return result
