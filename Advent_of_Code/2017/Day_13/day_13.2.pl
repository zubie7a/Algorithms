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
    foreach my $layer_index (keys %{ $layers }) {
        my $depth = $layers->{$layer_index};
        # $limit is the amount of steps the scanner requires to go back
        # to position 0. If a layer has depth 4, then the steps the
        # scanner will take are:
        #    [0, 1, 2, 3, 2, 1]
        # So it takes 6 steps before resetting. The packet can only
        # move in position 0 of layers, so use the formula to check
        # what will be the position of the scanner when packet arrives
        # to its layer.
        my $limit = ($depth - 1) * 2;
        # $delay + $layer_index is the amount of steps the packet
        # has to take for reaching the layer.
        my $scanner_pos = ($delay + $layer_index) % $limit;
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
