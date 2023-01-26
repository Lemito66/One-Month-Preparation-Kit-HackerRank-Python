def matching_strings(strings: list , queries: list):
    results = []
    for query in queries:
        count = 0
        for string in strings:
            if query == string:
                count +=1
        results.append(count)
    return results

print(matching_strings(['ab','ab','abc'],['ab','abc','bc']))
