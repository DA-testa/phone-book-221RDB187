#Evita Celmina 221RDB187

def read_queries():
    n = int(input("n? "))
    return [input().split() for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query[0] == 'add':
            contacts[cur_query[1]] = cur_query[2]
        elif cur_query[0] == 'del':
            if cur_query[1] in contacts:
                del contacts[cur_query[1]]
        else:
            response = contacts.get(cur_query[1], 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
