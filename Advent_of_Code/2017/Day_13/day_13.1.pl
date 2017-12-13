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

# Each hash position contains:
# A layer, and a flag denoting the scanner direction and
# current position. THIS WILL RUN AN UGLY SIMULATION,
# OPTIMIZE!
my $layers = {};
# The deepest layer.
my $max_index = -1;
foreach my $scanner (@{ $scanners }) {
    my ($index, $depth) = split ": ", $scanner;
 
    my $layer = {};
    $layer->{scanner_pos} = 0;
    $layer->{scanner_dir} = 1;
    $layer->{depth} = $depth;

    # Store this layer.
    $layers->{$index} = $layer;
    $max_index = $index if $index > $max_index;
}

# This is the result of multiplying the index of each layer in
# which the firewall encountered the packet and the depth of
# each layer where it happened.
my $severity = 0;
my $caught = 0;
# Each iteration will take "one pico-second", which is the
# time it takes to the packet to move and also for the
# scanners to move.
for (0 .. $max_index) {
    my $pak_index = $_;
    # Now advance all scanners in all layers.
    # my $positions = [];
    for (0 .. $max_index) {
        my $index = $_;
        my $layer = $layers->{$_};
        # Skip layer indexes that don't have scanner information.
        # push @{ $positions }, "*" unless $layer;
        next unless $layer;

        my $depth = $layer->{depth};
        my $scanner_pos = $layer->{scanner_pos};
        my $scanner_dir = $layer->{scanner_dir};
        $caught = 1 if $index == $pak_index && $scanner_pos == 0;
        $severity += ($index * $depth) if $index == $pak_index && $scanner_pos == 0;
        # push @{ $positions }, $scanner_pos;

        $scanner_dir = -1 if $scanner_pos + 1 == $depth && $scanner_dir ==  1;
        $scanner_dir =  1 if $scanner_pos     == 0      && $scanner_dir == -1;
        $layer->{scanner_pos} = $scanner_pos + $scanner_dir;
        $layer->{scanner_dir} = $scanner_dir;
    }
    # Debugging:
    # Print in which layer is the packet, and which index is the scanner.
    #   (0)[0][*][*][0][*][0]
    #   [1](1)[*][*][1][*][1]
    #   [2][0](*)[*][2][*][2]
    #   [1][1][*](*)[3][*][3]
    #   [0][0][*][*](2)[*][2]
    #   [1][1][*][*][1](*)[1]
    #   [2][0][*][*][0][*](0)
    #
    #  my $line = "";
    #  foreach my $position (0 .. scalar @{ $positions } - 1) {
    #     my ($open, $close) = ("[", "]");
    #     if ($position == $pak_index) {
    #         ($open, $close) = ("(", ")");
    #     }
    #     $line .= $open . $positions->[$position] . $close;
    # }
    # $line .= "\n";
    # print $line;

}

# Result: 2160.
print "$severity\n";

# This same previous code is USELESS for 13.2, as its always simulating
# moving all the scanners, 13.2 result is in the millions and this code
# was just trying thousands after 10 minutes... So did 13.2 from scratch
# without simulating all of the steps but figuring out a formula.
# Optimization based on improvement of 13.2.

# Reset $severity to find it again with optimization.
$severity = 0;
$layers = {};
foreach my $scanner (@{ $scanners }) {
    my ($index, $depth) = split ": ", $scanner;
    $layers->{$index} = $depth;
}

my $delay = 0;
# Who knows, this may never stop...
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
    my $scanner_pos = $layer_index % $limit;
    $severity += $depth * $layer_index if $scanner_pos == 0;
}

# Result: 2160.
print "$severity\n";
