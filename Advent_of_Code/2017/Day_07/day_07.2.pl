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

# Now that we now the root animal, we have to start iterating at it
# on the regular tree to find the cumulative weights at each disk.
# It can be assumed that only one animal is out of balance, but all
# the animals holding it will also be out of balance, so the culprit
# is the one deepest into the tree, so a deep recursion will find it
# being the first found out of balance animal.
my $unbalanced_animal;
my $expected_weight;
my $unbalanced_weight;
sub calculate_weight {
    my ($animal) = @_;
    return 0 unless $animal;
    my $current_weight = $weight->{$animal};
    my $disc_names     = $circus->{$animal};
    if ($disc_names) {
        my @disc_names_list = map { ($_ =~ /\s*(.*)\s*/) } split ",", $disc_names;
        my $tower_animal_weights = {};
        my $tower_weight = 0;
        foreach my $disc_animal (@disc_names_list) {
            my $disc_animal_weight = calculate_weight($disc_animal);
            push @{ $tower_animal_weights->{$disc_animal_weight} }, $disc_animal;
            $tower_weight += $disc_animal_weight;
        }
        if (scalar (keys %{ $tower_animal_weights }) > 1) {
            # Only care about the first unbalanced animal found deep into the recursion.
            if (!$unbalanced_animal) {
                foreach my $weight (keys %{ $tower_animal_weights }) {
                    my @animals_with_weight = @{ $tower_animal_weights->{$weight} };
                    if ((scalar @{$tower_animal_weights->{$weight}}) == 1) {
                        ($unbalanced_animal) = @animals_with_weight;
                        $unbalanced_weight = $weight;
                    } else {
                        $expected_weight = $weight;
                    }
                }
            }
        }
        $current_weight += $tower_weight; 
    }
    return $current_weight;
}

calculate_weight($animal_name);

if ($unbalanced_animal) {
    my $animal_weight = $weight->{$unbalanced_animal};
    my $proper_weight = $animal_weight + ($expected_weight - $unbalanced_weight);
    # Result: 1215 + (1614 - 1623) == 1206.
    print "$proper_weight\n";
}
