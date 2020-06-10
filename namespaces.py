requests = []

namespaces = [{'name': 'global', 'parent': 'namespaces', 'children': []}]

def parse_input(req):
    
    request = req.split()
    method = request[0]
    namespace = request[1]
    var = request[2]

    if method == 'create':
        add(namespace, var)
    if method == 'add':
        add(namespace, var)
    if method == 'get':
        print(get(namespace, var))

def add(namespace, var):
    
    for item in namespaces:
        if item['name'] == namespace:
            item['children'].append(var)
    
    element = {
        'name': var,
        'parent': namespace,
        'children': [] 
        }
    
    namespaces.append(element)

def get(namespace, var):
    
    for item in namespaces:
        if item['name'] == namespace:
            if var in item['children']:
                return item['name']
            else:
                rec = get(item['parent'], var) 
                return rec

q = int(input())
for i in range(q):
    requests.append(str(input()))

for item in requests:
    parse_input(item)
