use strict;
use warnings;

# The target value we are looking for: 
my $target = 265149;

# Dimensions for grid of 1000x1000.
my ($width, $height) = (100, 100);

# Create a $height * $width grid full of 0s.
my $grid = [ map { [ map { 0 } 0 .. $width ] } 0 .. $height ];

# Put a initial 1 in the middle of the grid. 
my ($x, $y) = ($width / 2, $height / 2);
$grid->[$x]->[$y] = 1;

# Current segment length and a flag to determine whether to increase it.
# The segment will only be increased every two times a segment is completed.
my ($segment, $increase) = (1, 0);
# Four possible directions, initial one is 0 ~ right.
my ($dir_index, $dirs) = (0, ["r", "u", "l", "d"]);

# To check for neighbors easily, iterating twice over this to get dx/dy.
my $deltas = [-1, 0, 1];

# How much of a segment have we traversed.
my $partial_segment = 0;
# We'll basically start generating all values spiraling out from the
# center until we exceed our target.
for (0 .. $width * $height) {
    my $dir = $dirs->[$dir_index];
    $x += 1 if $dir eq "r";
    $y -= 1 if $dir eq "u";
    $x -= 1 if $dir eq "l";
    $y += 1 if $dir eq "d";
    $partial_segment += 1;
    # Reached the end of the segment, change direction.
    if ($partial_segment == $segment) {
        $partial_segment = 0;
        # Increase segment length only every two segments.
        $segment += 1 if $increase;
        $increase = !$increase;
        # Change the direction for next iteration.
        $dir_index = ($dir_index + 1) % 4;
    }
    # Value at this (x, y) position is the sum of all neighbors so far
    # while spiraling out, not any not yet visited square. To make it easy
    # will check in every direction but not yet visited squares are 0 :-)
    my $value = 0;
    foreach my $dx (@{ $deltas }) {
        foreach my $dy (@{ $deltas }) {
            my ($_x, $_y) = ($x + $dx, $y + $dy);
            next if ($_x < 0 || $_x >= $width);
            next if ($_y < 0 || $_y >= $height);
            $value += $grid->[$_x]->[$_y];
        }
    }

    $grid->[$x]->[$y] = $value;
    if ($value > $target) {
        # Result: 266330.
        print "$value\n";
        last;
    }
}
