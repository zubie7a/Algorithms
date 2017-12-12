use strict;
use warnings;

my $input;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $input = [split ',', $line];
}

close($file_in);

# The original values of the circular ribbon.
my $values = [0 .. 255];
# Test final values: $values == [3, 4, 2, 1, 0].
my $test_input = [3, 4, 1, 5];
# The position from which to start folding according to a length,
# and the skip value to jump larger and larger.
my ($pos, $skip) = (0, 0);
# Input will be the list of lengths of segments to fold/revert.
foreach my $length (@{ $input }) {
    # my $list_to_revert = [];
    # Build the list to revert (wrapping around) inside segment
    # with given length.
    # foreach my $delta (0 .. $length - 1) {
    #     my $new_pos = ($pos + $delta) % (scalar @{ $values });
    #     push @{ $list_to_revert }, $values->[$new_pos];
    # }
    # @{ $list_to_revert } = reverse @{ $list_to_revert };
    # # Now within the same segment in original list, replace values
    # # (again wrapping around) in the reversed order.
    # foreach my $delta (0 .. $length - 1) {
    #     my $new_pos = ($pos + $delta) % (scalar @{ $values });
    #     $values->[$new_pos] = $list_to_revert->[$delta];
    # }
    # $list_to_revert = [];

    # In-Place version of reverse swap:
    foreach my $delta (0 .. $length / 2 - 1) {
        my $values_length = scalar @{ $values };
        my $base = $pos + $values_length;
        my $old = ($base + $delta) % $values_length;
        my $new = ($base + ($length - 1) - $delta) % $values_length;
        ($values->[$old], $values->[$new]) = ($values->[$new], $values->[$old]);
    }

    # Increase the position by the segment length and the skip value.
    $pos += $length + $skip;
    # Then increase the skip value so that every jump in the future
    # is increasingly larger.
    $skip += 1;
}

# Result: 38415.
my $res = $values->[0] * $values->[1];
print "$res\n";
