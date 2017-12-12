use strict;
use warnings;

# [0, 2, 7, 0], each position is a memory bank with n blocks.
# Find the one with most blocks, if tie, then lower indexed
# position is the one with prevalence. At first, '7' (memory
# bank at pos 2) has the most blocks. Then the position is
# put to 0 and the 7 blocks will be spread one by one, 1 to
# 3rd, 1 to 0th, 1 to 1st. 1 to 2nd (original), 1 to 3rd,
# 1 to 0th, 1 to 2nd. Now its [2, 4, 1, 2].

# Now starting again the 2nd bank has the most blocks so its
# used for redistribution and so on. The problem is that this
# program can be caught in an infinite loop since from some
# states, the same state could be reached again after x steps.

my $memory = [
    # Result: 5
    [0, 2, 7, 0],
    # Result: 6681.
    [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3],
];

sub row_to_string {
    # [0, 2, 7, 0] => "0 2 7 0" for hashing and storing states.
    my ($row) = @_;
    return join " ", @{ $row };
}

foreach my $memory_row (@{ $memory }) {
    my $seen_before = {};
    # Total of iterations it takes until reaching a repeated state.
    my $iterations = 0;
    # Now start the endless redistribution.
    # Is this program guaranteed to halt? :-P
    while (1) {
        # Hash the current state.
        my $current_state = row_to_string($memory_row);
        # Exit infinite loop if state was seen before.
        last if defined $seen_before->{$current_state};
        # Now mark this state as seen.
        $seen_before->{$current_state} = 1;

        # Scan to find the highest value and start from there.    
        my $high_value = -1;
        my $high_index = -1;
        foreach my $pos (0 .. scalar @{ $memory_row} - 1) {
            my $value = $memory_row->[$pos];
            if ($value > $high_value) {
                $high_value = $value;
                $high_index = $pos;
            }
        }

        # Get the value to redistribute.
        my $memory_to_redistribute = $memory_row->[$high_index];
        # Set the value in the memory as 0.
        $memory_row->[$high_index] = 0;
        # Set the position to iterate from.
        my $index = $high_index;
        # Start redistributing all these memory blocks.
        while ($memory_to_redistribute) {
            # Iterate over the memory banks and wrap around if needed.
            $index = ($index + 1) % (scalar @{ $memory_row });
            # Increase the memory of the current block.
            $memory_row->[$index] += 1;
            # Decrease the memory left to redistribute.
            $memory_to_redistribute -= 1;
        }
        $iterations += 1;
    }
    print "$iterations\n";
}
