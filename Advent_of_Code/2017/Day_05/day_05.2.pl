use strict;
use warnings;

my $instructions = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $instructions }, $line;
}

close($file_in);

my $index = 0;
my $steps = 0;
while (0 <= $index && $index < scalar (@{ $instructions })) {
    my $delta = $instructions->[$index];
    # Same as before, but now if an instruction gets to a value of 3 or more, decrease
    # it by one, otherwise just increase it by one. This feels too brute-forcey :-(
    $instructions->[$index] += ($delta >= 3)? -1 : 1;
    $index += $delta;
    $steps += 1;
}
# Result: 25136209.
print "$steps\n";
