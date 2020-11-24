I am just so excited about this.

.. container:: separator

   ` <https://www.cs.drexel.edu/~bls96/museum/cardiac2-s.jpg>`__

.. container:: separator

.. container:: separator

   CARDIAC. The Cardboard Computer. How cool is that? This piece of
   history is amazing and better than that: it is extremely accessible.
   This fantastic design was built in 1969 by David Hagelbarger at Bell
   Labs to explain what computers were to those who would otherwise have
   no exposure to them. Miraculously, the CARDIAC (CARDboard Interactive
   Aid to Computation) was able to actually function as a slow and
   rudimentary computer. 

One of the most fascinating aspects of this gem is that at the time of
its publication the scope it was able to demonstrate was actually useful
in explaining what a computer was. Could you imagine trying to explain
computers today with anything close to the CARDIAC?
It had 100 memory locations and only ten instructions. The memory held
signed 3-digit numbers (-999 through 999) and instructions could be
encoded such that the first digit was the instruction and the second two
digits were the address of memory to operate on. The only register was
an accumulator.
The simple instruction set would have made for a very easy understanding
of how complex programs are able to be built out of simpler sets of
operations and data.
====== ======== ============================================
Opcode Mnemonic Operation
====== ======== ============================================
0      INP      Read a card into memory
1      CLA      Clear accumulator and add from memory (load)
2      ADD      Add from memory to accumulator
3      TAC      Test accumulator and jump if negative
4      SFT      Shift accumulator
5      OUT      Write memory location to output card
6      STO      Store accumulator to memory
7      SUB      Subtract memory from accumulator
8      JMP      Jump and save PC
9      HRS      Halt and reset
====== ======== ============================================

There is a\ `much longer write
up <https://www.cs.drexel.edu/~bls96/museum/cardiac.html>`__\ that
anyone interested in the beginnings of computers should take a read
over. I am hoping to make up my own DIY CARDIAC and try writing some fun
programs and if I do I'm going to be sure to post about it.
