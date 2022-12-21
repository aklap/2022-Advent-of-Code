lines = open('../inputs/test.txt', 'r').read().splitlines()
signals = [line for line in lines]


def find_marker_end(signals, size):
    MARKER_SIZE = size
    indices = []
    for signal in signals:
        for i in range(0, len(signal)):
            if len(set(signal[i:i + MARKER_SIZE])) == MARKER_SIZE:
                indices.append(i + MARKER_SIZE)
                break
    return indices


print(*find_marker_end(signals, 4))
print(*find_marker_end(signals, 14))