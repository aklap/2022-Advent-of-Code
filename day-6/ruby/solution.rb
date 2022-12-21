lines = File.open('../inputs/test.txt').readlines.map(&:chomp)

def get_marker_index(lines, packet_size)
    lines.map do |line|
        _, match_idx = line.chars
                            .each_cons(packet_size)
                            .with_index
                            .find { |str, i| str.uniq.size == packet_size }
        match_idx + packet_size
    end
end

puts "Markers ending at the following indices for packet size 4: #{get_marker_index(lines, 4).join(', ')}."
puts "Markers ending at the following indices for packet size 14: #{get_marker_index(lines, 14).join(', ')}."