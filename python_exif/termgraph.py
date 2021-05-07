
def render(data: list, width = 40):
    if not data:
        return
    key_length = max(len(key) for key, _ in data)
    graph_length = width - key_length - 2
    max_value = max(value for _, value in data)
    per_value = max_value / graph_length
    for key, value in data:
        if value == 0:
            continue
        key_str = format(key, f' >{key_length}')
        graph = int(value / per_value)
        value_str = format(str(value), f'▇<{graph}')
        print(f'{key_str}: {value_str}')


def main():
    render([('A', 12), ('BC', 24), ('DEF', 36)])
    render([])
