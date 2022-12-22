def sum_group(rucksacks)
  rucksacks.reduce(0) do |sum, rucksack|
    left = (rucksack[0...(rucksack.size / 2)]).chars
    right = (rucksack[(rucksack.size / 2)..]).chars
    item = (left & right).first
    sum + get_score(item)
  end
end

def sum_three_groups(rucksacks)
  rucksacks.each_slice(3).reduce(0) do |sum, slice|
    trio = slice.map(&:chars)
    sum + get_score((trio[0] & trio[1] & trio[2]).first)
  end
end

def get_score(item)
  item.ord - (item.ord <= 90 ? 38 : 96)
end

def display_total(sum)
  puts "The sum of common items was: #{sum}"
end

rucksacks = File.open('../inputs/input.txt').read.split("\n")
display_total(sum_group(rucksacks))
display_total(sum_three_groups(rucksacks))