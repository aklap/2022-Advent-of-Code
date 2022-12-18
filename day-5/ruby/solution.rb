lines  = File.read('../inputs/input.txt').split("\n\n")
# Create instructions
def get_instructions(lines)
    instructions = lines[1].split("\n").map { |instruct| instruct.scan(/\d+/).map(&:to_i) }
end
# Create rows
def get_rows(lines)
    rows = lines[0].split("\n")[0..-2].map{ |row| row.gsub(/[\[\]]/, ' ') }
end
# Create stacks, transpose rows
def transpose(rows)
    n_chars = 0..rows.first.size
    n_chars.step(4).map do |start|
        rows.reduce([]) do |stacks, row|
            stack = row[start..start+3].gsub(' ', '')
            stack.scan(/[A-Z]/).any? ? stacks << stack : stacks
        end 
    end
end
# move one crate
def move_one(stacks, n, move_start, move_end)
    n.times do
        removed = stacks[move_start].shift
        stacks[move_end].unshift(removed)
    end
    stacks
end
# move multiple crates
def move_multiple(stacks, n, move_start, move_end)
    removed = stacks[move_start].slice!(0, n)
    stacks[move_end].unshift(*removed)
    stacks
end
# move crates
def move_crates(stacks, instructions, options={})
    instructions.each do |instruction|
        n_crates = instruction[0]
        move_start = instruction[1] - 1
        move_end = instruction[2] - 1
        if options[:one]
            stacks = move_one(stacks, n_crates, move_start, move_end)
        end
        if options[:multiple]
            stacks = move_multiple(stacks, n_crates, move_start, move_end)
        end
    end
    stacks
end
# Prints message from moved crates
def display_message(stacks)
    puts "Message is #{ stacks.map(&:first).join('') }"
end

rows = get_rows(lines)
stacks = transpose(rows) 
instructions = get_instructions(lines)
# test one
moved = move_crates(stacks, instructions, one: true)
display_message(moved)
# reset
stacks = transpose(rows)
# test multiple
moved = move_crates(stacks, instructions, multiple: true)
display_message(moved)