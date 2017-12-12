use strict;
use warnings;

my $lines = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $lines }, $line;
}

close($file_in);

my $result = 0;

foreach my $line (@{ $lines }) {
    my @words = split ' ', $line;

    sub sort_chars {
        my ($word) = @_;
        # Split by characters, sort them, and then append them again.
        my $new_word = join "", (sort (split //, $word));
        return $new_word;
    }
    # To find anagram words, take each word and sort its characters before storing it.
    my %dict = map { sort_chars($_) => 1 } @words;
    # After grouping by unique occurrences, the amount of words must be the same as the
    # words in the original list to ensure there's no duplicates.
    $result += (scalar (keys %dict)) == (scalar @words);
}

# Result: 251.
print "$result\n";
