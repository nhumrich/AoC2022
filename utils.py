def read_input(day, test=False):
    with open(f'../{day}/{"test" if test else "main"}.input') as f:
        return f.read()
