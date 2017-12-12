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
    # Since we're only comparing individual digits, and the list is circular,
    # then put the first digit at the end of the list too.
    push @digits, $digits[0];

    my $result = 0;
    my $length = scalar @digits;
    foreach my $pos (0 .. $length - 2) {
        my ($this, $next) = ($digits[$pos], $digits[$pos + 1]);
        $result += $this * ($this == $next);
    }    
    # Results: 3, 4, 0, 9, 1136.
    print "$result\n";
}

# Version with a list with sum + map.
foreach my $input (@{ $inputs }) {
    my @digits = split //, $input;
    # Since we're only comparing individual digits, and the list is circular,
    # then put the first digit at the end of the list too.
    push @digits, $digits[0];

    # Return digit at position if its equal to digit in next position.
    my $compare = sub {
        my ($pos) = @_;
        return $digits[$pos] * ($digits[$pos] == $digits[$pos + 1]);
    };
    my $length = scalar @digits;
    my $result = sum( map { $compare->($_) } (0 .. $length - 2) );
    # Results: 3, 4, 0, 9, 1136.
    print "$result\n";
}

# Version with a hash of counts.
foreach my $input (@{ $inputs }) {
    my $matches = {};
    my @digits = split //, $input;
    # Since we're only comparing individual digits, and the list is circular,
    # then put the first digit at the end of the list too.
    push @digits, $digits[0];

    my $length = scalar @digits;
    foreach my $pos (0 .. $length - 2) {
        my ($this, $next) = ($digits[$pos], $digits[$pos + 1]);
        # If current digit matches the next one, increase occurrences of it.
        $matches->{$this} += 1 if $this == $next;
    }
    my $result = 0;
    # The result is adding up all the digits that matched the next digit,
    # times the amount of occurrences of such digits.
    foreach my $key (keys %{ $matches }) {
        my $value = $matches->{$key};
        $result += $key * $value;
    }
    # Results: 3, 4, 0, 9, 1136.
    print "$result\n";
}
