signals = open('../inputs/test.txt', 'r').read().splitlines()


def find_marker_end(signals, marker_size):
    indices = []
    for signal in signals:
        for i in range(len(signal)):
            if len(set(signal[i:i + marker_size])) == marker_size:
                indices.append(i + marker_size)
                break
    return indices


print("Signals start at indices: {}".format(find_marker_end(signals, 4)))
print("Signals start at indices: {}".format(find_marker_end(signals, 14)))
