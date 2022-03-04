  1           0 LOAD_CONST               0 (<code object main at 0x564456b6b9c0, file "example.py", line 1>)
              2 LOAD_CONST               1 ('main')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (main)

 15           8 LOAD_NAME                0 (main)
             10 CALL_FUNCTION            0
             12 POP_TOP
             14 LOAD_CONST               2 (None)
             16 RETURN_VALUE

Disassembly of <code object main at 0x564456b6b9c0, file "example.py", line 1>:
  2           0 LOAD_GLOBAL              0 (input)
              2 LOAD_CONST               1 ("What's the password? ")
              4 CALL_FUNCTION            1
              6 STORE_FAST               0 (inp)

  3           8 LOAD_CONST               2 ('')
             10 STORE_FAST               1 (pwd)

  4          12 SETUP_LOOP              52 (to 66)
             14 LOAD_GLOBAL              1 (range)
             16 LOAD_GLOBAL              2 (len)
             18 LOAD_FAST                0 (inp)
             20 CALL_FUNCTION            1
             22 CALL_FUNCTION            1
             24 GET_ITER
        >>   26 FOR_ITER                36 (to 64)
             28 STORE_FAST               2 (i)

  5          30 LOAD_FAST                1 (pwd)
             32 LOAD_GLOBAL              3 (chr)
             34 LOAD_GLOBAL              4 (ord)
             36 LOAD_FAST                0 (inp)
             38 LOAD_FAST                2 (i)
             40 BINARY_SUBSCR
             42 CALL_FUNCTION            1
             44 LOAD_FAST                2 (i)
             46 LOAD_GLOBAL              5 (int)
             48 LOAD_CONST               3 (7)
             50 CALL_FUNCTION            1
             52 BINARY_MODULO
             54 BINARY_ADD
             56 CALL_FUNCTION            1
             58 INPLACE_ADD
             60 STORE_FAST               1 (pwd)
             62 JUMP_ABSOLUTE           26
        >>   64 POP_BLOCK

  6     >>   66 LOAD_CONST               4 (102)
             68 LOAD_CONST               5 (109)
             70 LOAD_CONST               6 (99)
             72 LOAD_CONST               7 (106)
             74 LOAD_CONST               8 (127)
             76 LOAD_CONST               9 (53)
             78 LOAD_CONST              10 (116)
             80 LOAD_CONST              11 (95)
             82 LOAD_CONST              12 (122)
             84 LOAD_CONST              13 (113)
             86 LOAD_CONST              14 (120)
             88 LOAD_CONST              15 (118)
             90 LOAD_CONST              16 (100)
             92 LOAD_CONST              17 (55)
             94 LOAD_CONST              18 (51)
             96 LOAD_CONST              19 (103)
             98 LOAD_CONST              20 (57)
            100 LOAD_CONST              21 (128)
            102 BUILD_LIST              18
            104 STORE_FAST               3 (comp)

  7         106 LOAD_CONST              22 (False)
            108 STORE_FAST               4 (incor)

  8         110 SETUP_LOOP              58 (to 170)
            112 LOAD_GLOBAL              1 (range)
            114 LOAD_GLOBAL              2 (len)
            116 LOAD_FAST                1 (pwd)
            118 CALL_FUNCTION            1
            120 CALL_FUNCTION            1
            122 GET_ITER
        >>  124 FOR_ITER                42 (to 168)
            126 STORE_FAST               2 (i)

  9         128 LOAD_FAST                1 (pwd)
            130 LOAD_FAST                2 (i)
            132 BINARY_SUBSCR
            134 LOAD_GLOBAL              3 (chr)
            136 LOAD_FAST                3 (comp)
            138 LOAD_FAST                2 (i)
            140 BINARY_SUBSCR
            142 CALL_FUNCTION            1
            144 COMPARE_OP               3 (!=)
            146 POP_JUMP_IF_FALSE      160

 10         148 LOAD_GLOBAL              6 (print)
            150 LOAD_CONST              23 ('Incorrect password...')
            152 CALL_FUNCTION            1
            154 POP_TOP

 11         156 LOAD_CONST              24 (True)
            158 STORE_FAST               4 (incor)

 12     >>  160 LOAD_FAST                4 (incor)
            162 POP_JUMP_IF_FALSE      124
            164 BREAK_LOOP
            166 JUMP_ABSOLUTE          124
        >>  168 POP_BLOCK

 13     >>  170 LOAD_FAST                4 (incor)
            172 POP_JUMP_IF_TRUE       182
            174 LOAD_GLOBAL              6 (print)
            176 LOAD_CONST              25 ('Welcome!')
            178 CALL_FUNCTION            1
            180 POP_TOP
        >>  182 LOAD_CONST               0 (None)
            184 RETURN_VALUE