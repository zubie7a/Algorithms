use strict;
use warnings;

my $programs = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $programs }, $line;
}

close($file_in);


# Which program connects to which programs.
my $graph = {};

# Loop to create initial individual weights hash, circus tree and inverse tree.
foreach my $program_pipes (@{ $programs }) {
    my ($program, $programs) = split "<->", $program_pipes;
    # Trim spaces.
    $program  =~ s/^\s+|\s+$//g if $program;
    $programs =~ s/^\s+|\s+$//g if $programs;
    $program  //= "";
    $programs //= "";
    # Store the programs piped with a program as an array, bidirectionally.
    push @{ $graph->{$program} }, split ", ", $programs;
    foreach my $target (@{ $graph->{$program} // [] }) {
        next if $target eq $program;
        push @{ $graph->{$target} }, $program;
    }
}

# Find all programs reachable from every program, but skip loops
# and already visited programs. If visited at least one at each
# root, it means it wasn't visited before and its a new group.
my $visited = {};
my $groups = 0;

foreach my $root (keys %{ $graph }) {
    my $reachable = 0;
    my $queue = [$root];
    while (scalar @{ $queue }) {
        my $element = shift @{ $queue };
        # Skip if was already visited.
        next if $visited->{$element};
        # Mark it as visited.
        $visited->{$element} = 1;
        # Increase count of programs reachable from 0.
        $reachable += 1;
        # Put in the queue all neighbors.
        foreach my $target (@{ $graph->{$element} // [] }) {
            push @{ $queue }, $target;
        }
    }
    
    $groups += 1 if $reachable;
}

print "$groups\n";