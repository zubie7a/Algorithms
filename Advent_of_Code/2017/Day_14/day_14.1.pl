use strict;
use warnings;
use List::Util qw /reduce/;

my $seed_str;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $seed_str = $line;
}

close($file_in);

my $blocks = 0;
# String always begins with this.
my $head = [ map { ord($_) } split('', "$seed_str") ];
# String always ends with this.
my $tail = [17, 31, 73, 47, 23];

# Same logic as day_10.2 but modifying the original string with an
# index from 0 to 127 and then generating a dense hash for each string.
for (0 .. 127) {
    my $index = $_;
    # Compute the middle component of the string.
    my $middle = [ map { ord($_) } split('', "-$index") ];
    my $seed = [];
    # Build the initial seed array.
    push @{ $seed }, @{ $head };
    push @{ $seed }, @{ $middle };
    push @{ $seed }, @{ $tail };

    # The original values of the circular ribbon.
    my $values = [0 .. 255];

    # The position from which to start folding according to a length,
    # and the skip value to jump larger and larger.
    my ($pos, $skip) = (0, 0);

    # 64 rounds! Preserving the skip and position values from previous
    # iterations, don't reset!
    for (1 .. 64) {
        foreach my $length (@{ $seed }) {
            # In-Place version of reverse sublist swap wrapping around:
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
        my $bin = sprintf("%.8b", $xor_value);
        $dense_hash .= $bin;
    }

    # Count the ones in the rows, these are the enabled squares in the grid.
    $blocks += scalar(grep {$_ eq '1'} (split '', $dense_hash)) . "\n";
}

# Result: 8216.
print "$blocks\n";
