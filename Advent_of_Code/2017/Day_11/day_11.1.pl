use strict;
use warnings;
use List::Util qw / sum /;

my $steps;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $steps = [ split(',', $line) ];
}

close($file_in);

# Test final values: (s, s, sw).
# "se" and "sw" are merged into "s" twice.
my $test_input = ["se", "sw", "se", "sw", "sw"];

# If "-" then it cancels out. If some value then thats resulting
# merged move. If nothing results then can't be merged,
# e.g. can't reduce/merge with itself or immediate neighbor.
my $mappings = {
    "n" => {
        "s" => "--", "se" => "ne", "sw" => "nw",
    },
    "ne" => {
        "s" => "se", "sw" => "--", "nw" => "n",
    },
    "se" => {
        "n" => "ne", "nw" => "--", "sw" => "s",
    },
    "s" => {
        "n" => "--", "nw" => "sw", "ne" => "se",
    },
    "sw" => {
        "n" => "nw", "ne" => "--", "se" => "s",
    },
    "nw" => {
        "s" => "sw", "se" => "--", "ne" => "n",  
    },
};

# The counts of available steps for each direction.
my $counts = {};
# Count how much moves are of each kind in the input.
foreach my $step (@{ $steps }) {
    $counts->{$step} += 1;    
}

while (1) {
    # To keep track that something was merged or cancelled.
    my $changed = 0;
    foreach my $dir (keys %{ $mappings }) {
        # If there's movements of that available.
        # For every possible another movement which can be potentially
        # cancelled or reduced or not.
        foreach my $new (keys %{ $mappings }) {
            # Two movements of the same can't be merged.
            my $same = $dir eq $new;
            next if $same;
            if (($counts->{$dir} // 0) > 0 && ($counts->{$new} // 0) > 0) {                   
                # Try seeing if the two movements can merge or cancel.
                my $target = $mappings->{$dir}->{$new};
                # If the two moves can be merged.
                if ($target) {
                    # Something will be merged or cancelled.
                    $changed = 1;
                    # Consume the two previous movements.
                    $counts->{$dir} -= 1;
                    $counts->{$new} -= 1;
                    # Create one of the merged movement only if they didn't
                    # cancel out.
                    if ($target ne "--") {
                        $counts->{$target} += 1;
                    }
                }
            }
        }
    }
    # Until nothing was merged or cancelled anymore.
    last unless $changed;
}

# The sum of steps of non-cancelled non-merged directions.
print sum(values %{ $counts }) . "\n";
