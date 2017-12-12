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

# Starting at position 0, increase index by the "instruction" value. Then increase the
# "instruction" value by 1. If index exceeds the "instruction" list bounds, exit and
# print the amount of steps it took to reach it.
# ...
# my $instructions = [0, 3, 0, 1, -3];
# Result: 5.

my $index = 0;
my $steps = 0;
while (0 <= $index && $index < scalar (@{ $instructions })) {
    # Add to the index the current "instruction" value and increase the stored value.
    my $delta = $instructions->[$index];
    $instructions->[$index] += 1;
    $index += $delta;
    $steps += 1;
}
# Result: 342669.
print "$steps\n";
