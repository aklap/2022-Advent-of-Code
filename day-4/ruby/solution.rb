require 'set'

# Process the entire txt file to get count
def count_overlap(lines, option={})
    lines.reduce(0) do |count, line|
        id_pair = sanitize(line)
        a = id_pair.first
        b = id_pair.last
        count += ((is_overlapping(a, b, option)) ? 1 : 0)
    end
end

# Takes a line and removes punctuation. Returns an array of 2 arrays with 2 \ ints in the inner arrays representing ranges, for ex: [[1, 2], [3, 4]]
def sanitize(str)
    return str.strip()
                .gsub('-', ' ')
                .split(',')
                .map { |line| line.split(' ').map(&:to_i) }
end

# Takes two arrays of ints and an option about which condition to check for, \ returns boolean value
def is_overlapping(a, b, options={})
    a_range = (a.first..a.last)
    b_range = (b.first..b.last)
    if options[:contain]
        return a_range.cover?(b_range) || b_range.cover?(a_range)
    end
    if options[:overlap]
        return (a_range.to_set & b_range.to_set).any?
    end
end

# Pretty print the return value
def display(count)
    puts "The number of overlapping pairs are: #{count}"
end

lines = File.open('../inputs/input.txt').readlines(chomp:true)
display(count_overlap(lines, contain: true))
display(count_overlap(lines, overlap: true))