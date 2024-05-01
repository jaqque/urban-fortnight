#!/usr/bin/env ruby

while gets();

$_.sub!(/^\xEF\xBB\xBF/, '')
if $_.include? " - ";
  artist,rest=$_.split(/ - /,2);
  if rest.include? "(";
    track,junk,rest=rest.rpartition(" (");
    if rest.nil?;
       year="";
    else
       year,junk=rest.split(/\)/,2) 
       year.chomp!
    end;
  else
    track=rest.chomp;
    year="";
  end
else
  artist=year="";
  track=$_.chomp;
end;
puts "\"#{artist}\",\"#{track}\",\"#{year}\""

end
