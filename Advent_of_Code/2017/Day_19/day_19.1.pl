use strict;
use warnings;
use List::MoreUtils qw/ first_index /;

my $grid;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $grid }, [split '', $line];
}

close($file_in);

# Little packet going around, will visit letters in this order:
# A, B, C, D, E, F.
# It will keep the same direction, unless it reaches an intersection
# in which there will be no ambiguity regardless which side to turn,
# and there will be no dead-ends with no need to backtrack.
#
#        * (START)
#        |          
#        |  +--+    
#        A  |  C    
#    F---|--|-E---+ 
#        |  |  |  D 
#        +B-+  +--+ 
#
# The starting position will always be a "|" on the first row.
# There's no ambiguities, like crossings where there's more than one
# alternative or paths that are touching back to back.

my ($height, $width) = (scalar @{ $grid }, scalar @{ $grid->[0] });
my $row = 0;
my $col = first_index { $_ eq '|' } @{ $grid->[0] };
# The starting direction will be downwards on rows.
my $dir = {
    row => 1,
    col => 0,
};

# At a crossing, will change direction if position after the crossing
# doesn't have a piece that allows continued movement.
my $visited = "";

# While its within bounds and also doesn't land on an empty space.
while (
    0 <= $row && $row < scalar(@{ $grid }) &&
    0 <= $col && $col < scalar(@{ $grid->[0] }) &&
    $grid->[$row]->[$col] ne ' '
) {
    my $direction = ($dir->{row}) ? "vertical" : "horizontal";
    if ($grid->[$row]->[$col] eq '+') {
        if ($direction eq "vertical") {
            # Stop going vertically, and choose which horizontal side to turn.
            $dir->{row} = 0;
            # If at either bound then it must turn to the opposite side.
            $dir->{col} =  1 if $col - 1 == 0;
            $dir->{col} = -1 if $col + 1 == $width;
            # If not at any bound, then choose the non-empty side.
            if (!$dir->{col}) {
                $dir->{col} = ($grid->[$row]->[$col + 1] ne ' ') ? 1 : -1;
            }
        }
        if ($direction eq "horizontal") {
            # Stop going horizontally, and choose which vertical side to turn.
            $dir->{col} = 0;
            # If at either bound then it must turn to the opposite side.
            $dir->{row} =  1 if $row - 1 == 0;
            $dir->{row} = -1 if $row + 1 == $height;
            # If not at any bound, then choose the non-empty side.
            if (!$dir->{row}) {
                $dir->{row} = ($grid->[$row + 1]->[$col] ne ' ') ? 1 : -1;
            }
        }
    } elsif ($grid->[$row]->[$col] =~ /([a-zA-Z]+)/) {
        # If its a letter, keep track of which letters have been visited.
        $visited .= $grid->[$row]->[$col];
    } 
    $row += $dir->{row};
    $col += $dir->{col};
} 

# Result: MKXOIHZNBL.
print "$visited\n";
