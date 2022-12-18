lines = File.open('../inputs/input.txt').readlines.map(&:chomp)

def get_marker_index(lines, packet_size)
    lines.map do |line|
        _, match_idx = line.chars
                            .each_cons(packet_size)
                            .with_index
                            .find {|substr, i| substr.uniq.size == packet_size }
        match_idx + packet_size
    end
end

p get_marker_index(lines, 4)
p get_marker_index(lines, 14)