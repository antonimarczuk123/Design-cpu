

# Control section

* ### Fetch cycle

1. IAR e , MAR s , BUS1 , ACC s
2. RAM e , IR s
3. ACC e , IAR s

* ### ALU

<img src="img/ALU-instructions.png" alt="">

1. REG A e , TMP s
2. ALU decoder , REG B e , ACC s , FLAG s
3. ACC e , REG B s

* ### STORE

<img src="img/STORE-instructions.png" alt="">

1. REG A e , MAR s
2. RAM e , REG B s

* ### LOAD

<img src="img/LOAD-instructions.png" alt="">

1. REG A e , MAR s
2. REG B e , RAM s

* ### DATA

<img src="img/DATA-instruction.png" alt="">

1. IAR e , BUS1 , ACC s , MAR s
2. RAM e , REG B s
3. ACC e , IAR s

* ### JMPR

<img src="img/JMPR-instruction.png" alt="">

1. REG B e , IAR s

* ### JMP

<img src="img/JMP-instr.png" alt="">

1. IAR e , MAR s
2. RAM e , IAR s

* ### JUMP IF

<img src="img/JUMP-IF-instr.png" alt="">

1. IAR e , MAR s , BUS1 , ACC s
2. ACC e , IAR s
3. ( RAMe e , IAR s ) : IF

* ### CLF

<img src="img/CLF-instr.png" alt="">

* ### END

<img src="img/END-instr.png" alt="">






