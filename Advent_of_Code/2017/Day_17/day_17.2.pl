use strict;
use warnings;

# Number of steps to execute the operations.
my $steps = 50000000;
# Index to store the current position.
my $index = 0;
# To store the value right after zero.
my $after_zero;
# Length of the jump to make between positions, cyclically.
my $jump;

my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $jump = $line;
}

close($file_in);

foreach my $step (1 .. $steps) {
    my $buffer_size = $step;
    # Check if we land at index 1, to store the latest inserted value.
    $index = ($index + $jump) % $buffer_size + 1;
    # Is it safe to assume that 0 will always be at position 0?
    # This seems to work but I'm not sure why... So for now we're
    # assuming that whenever we land at index 1 after a jump,
    # index 0 always contains 0.
    $after_zero = $step if $index == 1;
}

print "$after_zero\n";
