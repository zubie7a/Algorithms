use strict;
use warnings;

my $animals = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $animals }, $line;
}

close($file_in);

# Which animal holds which animals.
my $circus = {};
# Whats an animal weight.
my $weight = {};

# Which animal is not hold by anyone?
# Make an inverse tree! Key are animal names and values the parent
# in regular tree.
my $inverse_circus = {};

# Loop to create initial individual weights hash, circus tree and inverse tree.
foreach my $animal_info (@{ $animals }) {
    my ($animal_pair, $disc_names) = split "->", $animal_info;
    # Trim spaces.
    $animal_pair =~ s/^\s+|\s+$//g if $animal_pair;
    $disc_names  =~ s/^\s+|\s+$//g if $disc_names;
    $animal_pair //= "";
    $disc_names  //= "";
    my ($animal_name, $animal_weight) = split " ", $animal_pair;
    # Remove ().
    $animal_weight  =~ s/^\(|\)$//g if $animal_weight;
    # Store the animals held by an animal as a string.
    $circus->{$animal_name} = $disc_names if $disc_names;
    $weight->{$animal_name} = $animal_weight if $animal_weight;

    if ($disc_names) {
        my @disc_animals = split ",", $disc_names;
        foreach my $disc_animal (@disc_animals) {
            $disc_animal =~ s/^\s+|\s+$//g;
            $inverse_circus->{$disc_animal} = $animal_name;
        }
    }
}

# Pick an animal at random and start going down the inverse tree, the
# last element should be the animal with no other animal holding it.
# We can assume that all the animals in input are part of the tree
# and no loops happen.
my $random_index = int(rand(scalar(keys %{ $inverse_circus })));
my $animal_name = (keys $inverse_circus)[$random_index];

# Find the bottom of the inverse tree, the root of original tree.
$animal_name = $inverse_circus->{$animal_name} while $inverse_circus->{$animal_name};

# Result: airlri.
print "$animal_name\n";
