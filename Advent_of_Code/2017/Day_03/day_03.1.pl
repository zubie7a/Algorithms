use strict;
use warnings;
use POSIX qw/ceil/;

# The value we want to find the "Manhattan Distance" of, that is the distance
# from the square this position happen and the original position [1], distributed
# along a spiral arrangement of numbers. 
my $inputs = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $value = <$file_in> ) {
    chomp $value;
    push @{ $inputs }, $value;
}

close($file_in);

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
