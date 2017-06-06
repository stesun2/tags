count = 0
IO::read("source-text").each_line do |l|
  File.open('text.txt', 'a') do |f|
    f.write l
    count+=1
  end
  puts `git add text.txt`
  snippet = l[0..20]
  puts `git commit -m 'Adding line #{count}: #{snippet}'`
end
