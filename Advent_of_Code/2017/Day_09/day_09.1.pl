use strict;
use warnings;

my $input;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    $input .= $line;
}

close($file_in);

# Result: 1.
my $garbage_test = '{<>,<jfdsklfjsdklfj>,<<<<>,<{!>}>,<!!>,<!!!>>,<{o"i!a,<{i<a>}';
# Result: 3.
my $groups_test = '{{<a!>},{<a!>},{<a!>},{<ab>}}';

my $invalid = 0;
my $garbage_flag = 0;

my $score = 0;
my $total_score = 0;
foreach my $char (split('', $input)) {
    # Stack the scores, increasingly.
    if ($char eq '{' && !$garbage_flag) {
        $score += 1;
    }
    if ($char eq '}' && !$garbage_flag) {
        $total_score += $score;
        $score -= 1;
    }

    # If '!' tell next char to skip, or if told by prev char to skip.
    # Will end up skipping both current '!' and the next character.
    if ($char eq '!' || $invalid) {
        $invalid = !$invalid;
        next;
    }
    $garbage_flag = 1 if $char eq '<';
    $garbage_flag = 0 if $char eq '>';
}

# Result: 14190.
print "$total_score\n";
