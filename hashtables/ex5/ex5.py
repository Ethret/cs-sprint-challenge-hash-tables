def finder(files, queries):
    path_dict = {}

    for path in files:
        split_strings = path.split("/")
        file_name = split_strings.pop()
        rest_of_path = "/".join(split_strings)
        if file_name in path_dict.keys():
            path_dict[file_name].append(rest_of_path)
        else:
            path_dict[file_name] = [rest_of_path]

    result = []

    for query in queries:
        if query in path_dict.keys():
            for path in path_dict[query]:
                found_file = (path + "/" + query)
                result.append(found_file)
        else:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
