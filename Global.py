import sys
sys.path.insert(0, './Model')

PRINT_QUERY = 0

def print_query(query):
    if PRINT_QUERY is not 0 : print(query)

def dict2var(dict, field):
    for row in dict:
        var = row[field]
    return var