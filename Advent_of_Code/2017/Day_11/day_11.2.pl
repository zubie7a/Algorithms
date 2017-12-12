use strict;
use warnings;
use List::Util qw / max /;

my $steps;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $steps = [ split(',', $line) ];
}

close($file_in);

# Super useful resource for understanding hexagonal distances:
# https://www.redblobgames.com/grids/hexagons/#distances
# Also see the image grid.png on this repo for understanding
# the change in "axis" and the "taxicab" distance of hex grids.
my ($x, $y, $z) = (0, 0, 0);
my $max_dist = 0;

foreach my $step (@{ $steps }) {
    $x += 1 if $step eq "se" || $step eq "ne";
    $y += 1 if $step eq "n"  || $step eq "nw";
    $z += 1 if $step eq "s"  || $step eq "sw";
    $x -= 1 if $step eq "sw" || $step eq "nw";
    $y -= 1 if $step eq "s"  || $step eq "se";
    $z -= 1 if $step eq "n"  || $step eq "ne";
    my $cur_dist = (abs($x) + abs($y) + abs($z)) / 2;
    $max_dist = max($cur_dist, $max_dist);
}

print "$max_dist\n";
