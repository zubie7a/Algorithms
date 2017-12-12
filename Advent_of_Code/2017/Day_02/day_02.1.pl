use strict;
use warnings;
use List::Util qw(
    max
    min
);

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
    my ($min, $max) = (min(@{ $row }), max(@{ $row }));
    my $diff = $max - $min;
    $checksum += $diff;
}

# Result: 32121.
print "$checksum\n";
