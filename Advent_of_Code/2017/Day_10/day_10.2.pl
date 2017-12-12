use strict;
use warnings;
use List::Util qw /reduce/;

my $ascii_input;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $ascii_input = [ map { ord($_) } split('', $line) ];
}
# Special lengths to be added at the end as per problem statement.
push @{ $ascii_input }, (17, 31, 73, 47, 23);

close($file_in);

# The original values of the circular ribbon.
my $values = [0 .. 255];
# Test dense hash result: 33efeb34ea91902bb2f59c9920caa6cd.
my $test_input = [ map { ord($_) } split('', "AoC 2017") ];
push @{ $test_input }, (17, 31, 73, 47, 23);
# The position from which to start folding according to a length,
# and the skip value to jump larger and larger.
my ($pos, $skip) = (0, 0);

# 64 rounds! Preserving the skip and position values from previous
# iterations, don't reset!
for (1 .. 64) {
    foreach my $length (@{ $ascii_input }) {
        # my $list_to_revert = [];
        # foreach my $delta (0 .. $length - 1) {
        #     my $new_pos = ($pos + $delta) % (scalar @{ $values });
        #     push @{ $list_to_revert }, $values->[$new_pos];
        # }
        # @{ $list_to_revert } = reverse @{ $list_to_revert };
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

        $pos += $length + $skip;
        $skip += 1;
    }
}

my $dense_hash = "";
# At this point the `values` make the "sparse" hash, now make it "dense"
# by taking groups of 16 elements and computing the XOR of each group
# and then converting that to HEX. There should be exactly 16 groups
# since `values` has a length of 256 elements.
for (0 .. 15) {
    my $start = $_ * 16;
    my $end = $start + 15;
    my @list = @{ $values }[$start .. $end];
    my $xor_value = reduce { $a ^ $b } @list;
    $dense_hash .= sprintf("%x", $xor_value);
}

# Result: 9de8846431eef262be78f590e39a4848.
print "$dense_hash\n";
