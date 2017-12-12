use strict;
use warnings;
use List::Util qw(sum);

my $inputs = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $value = <$file_in> ) {
    chomp $value;
    push @{ $inputs }, $value;
}

close($file_in);

# Version with a regular loop adding in-place.
foreach my $input (@{ $inputs }) {
    my @digits = split //, $input;
    my $length = scalar @digits;
    # We are assured that the string of digits has even length.
    my $middle = $length / 2;
    my $result = 0;
    foreach my $pos (0 .. $length - 1) {
        my ($i, $j) = ($pos, ($pos + $middle) % $length);
        my ($this, $next) = ($digits[$i], $digits[$j]);
        $result += $this * ($this == $next);
    }
    # Results: 6, 0, 4, 12, 4, 1092.
    print $result, "\n";
}

# Version with a list with sum + map.
foreach my $input (@{ $inputs }) {
    my @digits = split //, $input;
    my $length = scalar @digits;
    # We are assured that the string of digits has even length.
    my $middle = $length / 2;
    # Return digit at position if its equal to digit in next position.
    my $compare = sub {
        my ($pos) = @_;
        my $next = ($pos + $middle) % $length;
        return $digits[$pos] * ($digits[$pos] == $digits[$next]);
    };
    my $result = sum( map { $compare->($_) } (0 .. $length - 1) );
    # Results: 6, 0, 4, 12, 4, 1092.
    print "$result\n";
}
