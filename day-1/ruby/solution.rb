lines = File.open('../inputs/test.txt').read.split("\n\n")
calories_per_elf = lines.map { |l| l.split("\n").map(&:to_i).sum}.sort
puts "The highest calorie load was #{calories_per_elf.last}."
puts "The top 3 highest calorie loads were: %d, %d, and %d." % calories_per_elf.last(3)


