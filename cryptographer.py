while True:
 print('Programm cryptographer. Write "start" for begin')
 print('"exit" for exit')
 ans = input()
 if ans == 'start':
  while True:
   print('Write message.')
   message = input()
   cyph = ' '
   for ch in message:
            if ch == 'a' or ch == 'A':
                cyph +='0'
            elif ch == 'b' or ch == 'B':
                cyph +='1'
            elif ch == 'c' or ch == 'C':
                cyph +='2'
            elif ch == 'd' or ch == 'D':
                cyph +='3'
            elif ch == 'e' or ch == 'E':
                cyph +='4'
            elif ch == 'f' or ch =='F':
                cyph +='5'
            elif ch == 'g' or ch == 'G':
                cyph +='6'
            elif ch == 'h' or ch == 'H':
                cyph +='7'
            elif ch == 'i' or ch == 'I':
                cyph +='8'
            elif ch == 'j' or ch == 'J':
                cyph +='9'
            elif ch == 'k' or ch == 'K':
                cyph +='/'
            elif ch == 'l' or ch == 'L':
                cyph +='*'
            elif ch == 'm' or ch == 'M':
                cyph +='-'
            elif ch == 'n' or ch =='N':
                cyph +='+'
            elif ch == 'o' or ch == 'O':
                cyph +='.'
            elif ch == 'p' or ch == 'P':
                cyph +='!'
            elif ch == 'q' or ch == 'Q':
                cyph +='='
            elif ch == 'r' or ch == 'R':
                cyph +='|'
            elif ch == 's' or ch == 'S':
                cyph +='$'
            elif ch == 'T' or ch == 't':
                cyph +='%'
            elif ch == 'u' or ch == 'U':
                cyph +='@'
            elif ch == 'v' or ch =='v':
                cyph +='#'
            elif ch == 'w' or ch == 'W':
                cyph +='^'
            elif ch == 'x' or ch == 'X':
                cyph +='&'
            elif ch == 'y' or ch == 'Y':
                cyph +='('
            elif ch == 'z' or ch == 'Z':
                cyph +=')'
            elif ch =='0':
                cyph +='a'
            elif ch =='1':
                cyph +='b'
            elif ch =='2':
                cyph +='c'
            elif ch =='3':
                cyph +='d'
            elif ch =='4':
                cyph +='e'
            elif ch =='5':
                cyph +='f'
            elif ch =='6':
                cyph +='g'
            elif ch =='7':
                cyph +='h'
            elif ch =='8':
                cyph +='i'
            elif ch =='9':
                cyph +='j'
            elif ch == ' ':
                cyph += '_'
            elif ch == '!':
                cyph +=';'
            else:
                cyph +='~'
   break
  print('Your message')
  print(cyph)
 else:
     break
