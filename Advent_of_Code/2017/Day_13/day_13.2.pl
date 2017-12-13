use strict;
use warnings;

my $scanners = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $scanners }, $line;
}

close($file_in);

my $layers = {};
foreach my $scanner (@{ $scanners }) {
    my ($index, $depth) = split ": ", $scanner;
    $layers->{$index} = $depth;
}

my $delay = 0;
# Who knows, this may never stop...
while(1) {
    my $collisions = 0;
    foreach my $scanner (keys %{ $layers }) {
        my $depth = $layers->{$scanner};
        my $limit = ($depth - 1) * 2;
        my $scanner_pos = ($delay + $scanner) % $limit;
        $collisions += 1 if $scanner_pos == 0;
        last if $scanner_pos == 0;
    }
    # Result: 3907470.
    # real  0m58.606s
    # user  0m55.680s
    # sys   0m0.400s
    print "$delay\n" if $collisions == 0;
    last if $collisions == 0;
    $delay += 1;
}
