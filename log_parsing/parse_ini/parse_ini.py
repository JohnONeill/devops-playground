with open('data/inifile.ini') as file:
    cur_parent_key = '-'
    result_hash = {}
    for line in file:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue

        if line.startswith('[') and line.endswith(']'):
            cur_parent_key = line[1:-1]
            result_hash[cur_parent_key] = {}
        elif line.count('=') == 1:
            key, value = line.split('=')
            result_hash[cur_parent_key][key.strip()] = value.strip()

print(result_hash)
