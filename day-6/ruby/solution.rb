lines = File.open('../inputs/input.txt').readlines.map(&:chomp)

def get_marker_index(lines, packet_size)
    lines.map do |line|
        match = line.chars
                    .each_cons(packet_size)
                    .with_index.find {|sub, i| sub.uniq.size == packet_size }
        match.last + packet_size
    end
end

p get_marker_index(lines, 4)
p get_marker_index(lines, 14)