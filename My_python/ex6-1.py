def init(data):
    '初始化数据结构'
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    '获取人员姓名'
    return data[label].get(name)

def store(data, full_name):
    names=full_name.split()
    if len(names)==2:names.insert(1, '')
    labels='first', 'middle', 'last'

    for label, name, in zip(labels, names):
        people=lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]