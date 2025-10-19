# start of main.py

def extract_attributes(element):
    opener = ''
    final_attr = []
    
    for i, char in enumerate(element):
        if char == '>' and element[i-1] != '/':
            opener = element[1:i]
            break
        if char == '>' and element[i-1] == '/':
            opener = element[1:i-1]
            break

    el_list = opener.split()
    attributes = el_list[1:]

    for el in attributes:
        attr_name = ''
        attr_value = ''

        if '=' not in el:
            el = el.strip("'\"")
            final_attr[-1] = f"{final_attr[-1]} {el}"
        else:
            for i, char in enumerate(el):
                if char == '=':
                    attr_name = el[:i]
                    attr_value = el[i+1:].strip("'\"")

            final_attr.append(f"{attr_name}, {attr_value}")

    return final_attr

# end of main.py

