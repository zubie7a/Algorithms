use strict;
use warnings;

my $instructions;
my $filename = 'input.txt';
open(my $file_in, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
 
while (my $line = <$file_in>) {
    chomp $line;
    push @{ $instructions }, [split ' ', $line];
}

close($file_in);

# snd X: play sound with freq of val X.
# set X Y: sets reg X to Y (value or register value).
# add X Y: adds Y (value or register value) to reg X.
# mul X Y: mult reg X by Y (value or register value).
# mod X Y: mods reg X by Y (value or register value).
# rcv X: gets freq of last sound played IFF reg X is != 0.
# jgz X Y: jumps with an offset of Y, IFF reg X is > 0.

my $index = 0;
# Mappings of registers to values.
my $registers = {};
# Store the last played sound frequency.
my $sound_freq = 0;

while ($index < scalar(@{ $instructions })) {
    # All instructions have a command in its zero-th position.
    # All instructions have a register in its 1st position.
    # Just some instructions have a value in its 2nd position.
    my ($command, $register_name, $value) = @{ $instructions->[$index] };

    sub parse {
        my ($label) = @_;
        my $value = $label;
        if (defined $label && $label =~ /([a-zA-Z]+)/) {
            $value = $registers->{$label} // 0;
        }
        return $value;
    }

    my $regs_val = parse($register_name);
    my $oper_val = parse($value);

    if ($command eq "snd") {
        $sound_freq = $regs_val;
    } elsif ($command eq "set") {
        $registers->{$register_name} = $oper_val;
    } elsif ($command eq "add") {
        $registers->{$register_name} = $regs_val + $oper_val;
    } elsif ($command eq "mul") {
        $registers->{$register_name} = $regs_val * $oper_val;
    } elsif ($command eq "mod") {
        $registers->{$register_name} = $regs_val % $oper_val;
    } elsif ($command eq "rcv") {
        if ($regs_val) {
            $registers->{$register_name} = $sound_freq;
            last;
        }
    } elsif ($command eq "jgz") {
        if ($regs_val > 0) {
            $index += ($oper_val - 1);
        }
    }
    # Go to the next instruction.
    $index += 1;
}

# Result: 1187.
print "$sound_freq\n";
