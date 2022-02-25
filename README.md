# PIGS
PIGS is a minimalistic interpreted esolang based around pointers made by Y0UR-U5ERNAME. Its name originates from the four main commands in it: `P`, `I`, `G`, and `S`.

## Documentation
In PIGS, each command comes before its parameter. Commands include:
- `P`: Prints the corresponding character of the variable that the parameter points to. If this is impossible, then it prints nothing.
- `I`: Takes input starting with the variable that the parameter points to. The corresponding number of each character is stored.
- `G`: Starts running from a specific index of the commands, specified by the variable that the parameter points to. If the index goes past the end of the code, then the program is terminated.
- `S`: Prepares to set the variable that the variable that the parameter points to, points to. By default this is 0.
- `+`: Adds the variable that the parameter points to to the prepared variable.
- `-`: Subtracts the variable that the parameter points to from the prepared variable.
- `=`: Sets the prepared variable to 1 if it is equal to the variable that the parameter points to, otherwise 0.
- `:`: Sets the prepared variable to the variable that the variable that the parameter points to, points to.
- `#`: Sets the variable to the parameter.

Parameters are always binary numbers written with `0` and `1`. Variables are numbers that can be from 0 to 4294967295 (unsigned 32-bit).

All characters besides those described above are treated as comments.

## Examples
- [Hello, world!](https://esolangs.org/wiki/Hello,_world!): `#1001000P0#1100101P0#1101100P0P0#1101111P0#101100P0#100000P0#1110111P0#1101111P0#1110010P0#1101100P0#1100100P0#100001P0`
- [Truth-machine](https://esolangs.org/wiki/Truth-machine): `#1S0#10S1#11110S0#11S1#11100S0#100S1#110001S0#101S1#10S0#110I1S0#111S1#0+110=100+101:111P110G111`
- [Infinite loop](https://esolangs.org/wiki/Infinite_loop): `G0`
- [Cat program](https://esolangs.org/wiki/Cat_program): `#1S0#10S1#1000S0#101S1#11110S0+0S1#100101S0+0S1#10010I10S0#11S1:10=100+0+0+0+0+0:11G11:10P11S0#10S1+0G111`
