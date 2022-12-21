lines = open('../inputs/test.txt', 'r').read().splitlines()
signals = [line for line in lines]


def find_marker_end(signals, size):
    marker_size = size
    indices = []
    for signal in signals:
        for i in range(0, len(signal)):
            if len(set(signal[i:i + marker_size])) == marker_size:
                indices.append(i + marker_size)
                break
    return indices


print(*find_marker_end(signals, 4))
print(*find_marker_end(signals, 14))