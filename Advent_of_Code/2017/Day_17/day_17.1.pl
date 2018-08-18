use strict;
use warnings;

# Number of steps to execute the operations.
my $steps  = 2017;
# Index to store the current position.
my $index  = 0;
# Circular buffer that starts as [0] and starts growing.
my $buffer = [0];
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
    my $buffer_size = scalar @{ $buffer };
    # The index to insert at will be the next one right after jump.
    $index = ($index + $jump) % $buffer_size + 1;
    # Check whether its the end of the buffer to decide if splice or push.
    my $end_of_buf = ($index == $buffer_size); 
    # Can't splice at end of buffer, so just push value.
    push(@{ $buffer }, $step) if $end_of_buf;
    # Otherwise splice the value right into position after current.
    splice(@{ $buffer }, $index, 0, $step) if !$end_of_buf;

    # When its the last step, so its 2017...
    if ($step eq $steps) {
        # Give as result the value immediately afterwards.
        my $next_value = $buffer->[$index + 1];
        # Result: 640.
        print "$next_value\n";
    }
}
