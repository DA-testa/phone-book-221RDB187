#Evita Celmina 221RDB187

def read_queries():
    n = int(input("n? "))
    return [input().split() for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for _ in queries:
        if _[0] == 'add':
            contacts[_[1]] = _[2]
        elif _[0] == 'del':
            if _[1] in contacts:
                del contacts[_[1]]
        else:
            response = contacts.get(_[1], 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
