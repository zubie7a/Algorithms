use strict;
use warnings;

my $registers = {};
my $instructions = [];
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    # chomp $line;
    push @{ $instructions }, $line;
}

close($file_in);

sub validate {
    my ($cond_reg, $cond_comp, $cond_val) = @_;
    my $reg_val = $registers->{$cond_reg} // 0;
    
    return $reg_val == $cond_val if $cond_comp eq "==";
    return $reg_val != $cond_val if $cond_comp eq "!=";
    return $reg_val <= $cond_val if $cond_comp eq "<=";
    return $reg_val >= $cond_val if $cond_comp eq ">=";
    return $reg_val <  $cond_val if $cond_comp eq  "<";
    return $reg_val >  $cond_val if $cond_comp eq  ">";
}

# Since all registers start as 0, the minimum highest cumulative
# value at any point of time is 0, even after all registers turn
# negative.
my $max_value = 0;

sub operate {
    my ($reg, $op, $val) = @_;
    my $reg_value = $registers->{$reg} // 0;
    $max_value = $reg_value if $reg_value > $max_value;

    $registers->{$reg} += $val if $op eq "inc";
    $registers->{$reg} -= $val if $op eq "dec";
}

foreach my $instruction (@{ $instructions }) {
    my @elements = split " ", $instruction;
    # instruction example: "b inc 439 if yg >= -2142"
    my ($reg, $op, $val, $if, $cond_reg, $cond_comp, $cond_val) = @elements;
    operate($reg, $op, $val) if validate($cond_reg, $cond_comp, $cond_val);
}

# Print the max register value reached during processing.
# Result: 7037.
print "$max_value\n";
