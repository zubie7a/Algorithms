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

# snd X: send X to the other program (value or register value).
# set X Y: sets reg X to Y (value or register value).
# add X Y: adds Y (value or register value) to reg X.
# mul X Y: mult reg X by Y (value or register value).
# mod X Y: mods reg X by Y (value or register value).
# rcv X: receives value from other program into reg X..
# jgz X Y: jumps with an offset of Y, IFF reg X is > 0.

my $programs = {};
# Both programs have their own index in the instructions list,
# the queue of stuff received from the other program, and also 
# start with their own program_id stored in the register `p`,
# and are initially not labeled as waiting.
foreach my $id (0 .. 1) {
    $programs->{$id} = {
        program_id => $id,
        index => 0,
        registers => {
            p => $id,
        },
        is_waiting => 0,
        times_sent => 0,
        comm_queue => [],
    };
}

sub program_finished {
    my ($program) = @_;
    my $index = $program->{index};
    return $index >= scalar(@{ $instructions });
}

sub program_waiting {
    my ($program) = @_;
    return $program->{is_waiting};
}

sub queues_empty {
    my $len_p1 = scalar @{ $programs->{0}->{comm_queue} };
    my $len_p2 = scalar @{ $programs->{1}->{comm_queue} };
    return !($len_p1 + $len_p2);
}

sub execute {
    my ($program) = @_;

    my $index      = $program->{index};
    my $registers  = $program->{registers};
    my $program_id = $program->{program_id};

    # All instructions have a command in its zero-th position.
    # All instructions have a register or value in its 1st position.
    # Just some instructions have a value in its 2nd position.
    my ($command, $register_name, $value) = @{ $instructions->[$index] };
    # Check whether value its a scalar or another register, if a reg,
    # then retrieve the value and overwrite it.

    sub parse {
        my ($register_dict, $label) = @_;
        my $value = $label;
        if (defined $label && $label =~ /([a-zA-Z]+)/) {
            $value = $register_dict->{$label} // 0;
        }
        return $value;
    }

    my $regs_val = parse($registers, $register_name);
    my $oper_val = parse($registers, $value);

    if ($command eq "snd") {
        # Get the other program id, 0 => 1, 1 => 0.
        my $other_id = !$program_id + 0;
        my $other_program = $programs->{$other_id};
        push @{ $other_program->{comm_queue} }, $regs_val;
        $program->{times_sent} += 1;
    } elsif ($command eq "set") {
        $registers->{$register_name} = $oper_val;
    } elsif ($command eq "add") {
        $registers->{$register_name} = $regs_val + $oper_val;
    } elsif ($command eq "mul") {
        $registers->{$register_name} = $regs_val * $oper_val;
    } elsif ($command eq "mod") {
        $registers->{$register_name} = $regs_val % $oper_val;
    } elsif ($command eq "rcv") {
        if (scalar @{ $program->{comm_queue} }) {
            $program->{is_waiting} = 0;
            $registers->{$register_name} = shift $program->{comm_queue};
        } else {
            $program->{is_waiting} = 1;
        }
    } elsif ($command eq "jgz") {
        if ($regs_val > 0) {
            $index += ($oper_val - 1);
        }
    }
    # Go to the next instruction if program is not waiting at current one.
    $program->{index} = $index + 1 unless $program->{is_waiting};
}

while (1) {
    # Run each program as much as possible until it finishes or it waits.
    do {
        execute($programs->{0});
    } while 
        !program_finished($programs->{0}) 
     && !program_waiting($programs->{0});
    # To force them to behave "synchronously" despite their difference in speeds,
    # once a program needs something from the other and its waiting, it will remain
    # waiting as long as its required for the other program to send anything.
    do { 
        execute($programs->{1});
    } while 
        !program_finished($programs->{1}) 
     && !program_waiting($programs->{1});
    
    # Terminate execution if any of these conditions happen:
    #   * Both programs are finished.
    last if program_finished($programs->{0}) && program_finished($programs->{1});
    #   * Rither program has finished and the other is waiting.
    last if  program_waiting($programs->{0}) && program_finished($programs->{1});
    last if program_finished($programs->{0}) &&  program_waiting($programs->{1});
    #   * Both programs are waiting, the queues are empty.
    last if queues_empty()
         && program_waiting($programs->{0}) && program_waiting($programs->{1}); 
}

# Result: 5969.
print $programs->{1}->{times_sent} . "\n";
