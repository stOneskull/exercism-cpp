def transpose(input_lines):
    input_list = input_lines.split('\n')
    rows = len(input_list)
    columns = [[] * rows]
    for i, row in enumerate(input_list):
        for char in row:
            columns[i].append(char)
            print(char, columns)
    print([column.join() for column in columns].join('\n'))
