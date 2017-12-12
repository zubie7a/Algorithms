use strict;
use warnings;

my $input = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $input }, [split " ", $line];
}

close($file_in);

my $checksum = 0;
foreach my $row (@{ $input }) {
    my $length = scalar @{ $row };
    # Brute-force to compare all elements with all elements of row.
    foreach my $pos1 (0 .. $length - 2) {
        foreach my $pos2 ($pos1 + 1 .. $length - 1) {
            my ($val1, $val2) = ($row->[$pos1], $row->[$pos2]);
            # Swap to make sure $val1 is the larger one.
            ($val1, $val2) = ($val2,  $val1) if $val1 < $val2;
            $checksum     += ($val1 / $val2) if $val1 % $val2 == 0;
        }
    }
}

# Result: 197.
print "$checksum\n";
