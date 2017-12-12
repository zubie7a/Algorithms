use strict;
use warnings;
use List::Util 'max';


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

sub operate {
    my ($reg, $op, $val) = @_;
    $registers->{$reg} += $val if $op eq "inc";
    $registers->{$reg} -= $val if $op eq "dec";
}

foreach my $instruction (@{ $instructions }) {
    my @elements = split " ", $instruction;
    # instruction example: "b inc 439 if yg >= -2142"
    my ($reg, $op, $val, $if, $cond_reg, $cond_comp, $cond_val) = @elements;
    operate($reg, $op, $val) if validate($cond_reg, $cond_comp, $cond_val);
}

# Print the max register value at the end.
# Result: 4902.
print max (values %{ $registers }), "\n";
