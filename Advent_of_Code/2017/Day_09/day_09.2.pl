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

# Result: 32.
my $garbage_test = '{<>,<jfdskasdlfjsdklfj>,<<<<>,<{!>}>,<!!>,<!!!>>,<{o"i!a,<{i<a>}';
# Result: 17.
my $groups_test = '{{<a!>},{<a!>},{<a!>},{<ab>}}';

my $invalid = 0;
my $garbage_flag = 0;
my $garbage = '';
my $garbage_total = 0;

foreach my $char (split('', $input)) {
    # If '!' tell next char to skip, or if told by prev char to skip.
    # Will end up skipping both current '!' and the next character.
    if ($char eq '!' || $invalid) {
        $invalid = !$invalid;
        next;
    }
    if (!$garbage_flag && $char eq '<') {
        $garbage_flag = 1;
        next;
    }
    if ($char eq '>') {
        $garbage_flag = 0;
        $garbage_total += length($garbage);
        $garbage = '';
        next;
    }
    $garbage .= $char if $garbage_flag;
}

# Result: 7053.
print "$garbage_total\n";
