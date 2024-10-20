#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab15_2
# 204111 Sec 003

def unique_combo(heaps: list[tuple[str]]):
    return set(map(lambda x: (tuple(set(sorted(x)))), heaps))


if __name__ == '__main__':
    print(unique_combo([('red', 'green', 'blue', 'blue'),
                      ('blue', 'green', 'red'),
                      ('green', 'blue', 'red'),
                      ('pink', 'purple', 'orange','pink'),
                      ('orange', 'purple', 'pink')]))
    
