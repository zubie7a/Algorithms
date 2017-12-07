use strict;
use warnings;
use POSIX qw/ceil/;

# The value we want to find the "Manhattan Distance" of, that is the distance
# from the square this position happen and the original position [1], distributed
# along a spiral arrangement of numbers. 
my $inputs = [
    1, 12, 23, 1024, 265149,
];

foreach my $target (@{ $inputs }) {
    my ($iter, $increase)      = (1, 0);
    my ($pos_iter, $prev_iter) = (0, 0);
    my $pos = 1;
    while ($pos < $target) {
        $prev_iter =  $pos_iter;
        $pos      +=  $iter;
        $pos_iter  =  $iter;
        $iter += 1 if $increase;
        $increase  = !$increase;
    }

    my $mid_pos  = ceil($pos_iter  / 2);
    my $mid_prev = ceil($prev_iter / 2); 
    my $res = $mid_prev + abs($pos - $mid_pos - $target);
    # Results: 0, 3, 2, 31, 438.
    print "$res\n";
}

=cut

A spiraling out arrangement of numbers, starting at [1]:

37 36  35  34  33  32  31                   
38 17  16  15  14  13  30
39 18   5   4   3  12  29
40 19   6   1   2  11  28
41 20   7   8   9  10  27
42 21  22  23  24  25  26  ...
43 44  45  46  47  48  49  50

To reach any number on the grid, one must have completed a previous segment on
an axis and has a halfway or complete segment on next axis. Just knowing which
are the two segments containing+preceding the target value is enough information.

Segment progression until turning/pivot points:
1  +1 2   r
2  +1 3   u 
3  +2 5   l
5  +2 7   d
7  +3 10  r     To right: always odd.
10 +3 13  u     To up:    always odd.
13 +4 17  l     To left:  always even.
17 +4 21  d     To down:  always even.
21 +5 26  r
26 +5 31  u
31 +6 37  l
37 +6 43  d
73 +7 50  r

Distance to [1] in previous completed segment:
 * Since its a completed segment, its just the half of it, 
   cut segment length in half, and round up if odd.

Distance to [1] in current segment: 
 * Find value at the segment's middle: cut segment length in half, 
   substract from highest value in current segment.
 * Find the absolute difference of the value at middle of segment, 
   and the target value, giving the distance of value to middle.

Start increasing segments like...

[1] +1 +1 +2 +2 +3 +3 +4 +4 +5 +5 +6 +6 +7 +7 +...

Always keeping track of the current and previous segment, but stop when the target
value is reached or exceeded.

To reach 27:
 * horizontal +5 (to 26)           moving right => 3 ... 5/2 rounded up
 * vertical   +5 (to 31 - 4 == 27) moving up    => 1 ... abs(31 - (5/2 rounded up) - 27)

To reach 45:
 * vertical   +6 (to 43)           moving down  => 3 ... 6/2 (no round)
 * horizontal +7 (to 50 - 5 == 45) moving right => 1 ... abs(50 - (7/2 rounded up) - 45) 

To reach 38:
 * horizontal +6 (to 37)           moving left  => 3 ... 6/2 (no need to round or anything)
 * vertical   +6 (to 43 - 5 == 38) moving down  => 1 ... abs(43 - (6/2 no round) - 38)

To reach 36:
 * vertical   +5 (to 31)           moving up    => 3 ... 5/2 rounded up
 * horizontal +6 (to 37 - 1 == 36) moving left  => 1 ... abs(37 - (6/2 no round) - 36) 

=end
