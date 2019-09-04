def set_attr(content, value, attr):
    found = False
    for line in content:
        line = line.strip('\n')
        if line.startswith(f'#{attr}:'):
            found = True
            yield f'#{attr}:{value}\n'
        else:
            if not found and not line.startswith('#'):
                found = True
                yield f'#{attr}:{value}\n'
            yield f'{line}\n'
