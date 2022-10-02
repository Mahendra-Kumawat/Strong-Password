################  STRONG  PASSWORD #########


pas=input("enter password")
if len(pas)>8:
   if ("A"in pas or"B" in pas or"C" in pas or"D" in pas or"E"in pas or"F" in pas or"H" in pas or "I"in pas  or "J"in pas or "K"in pas or "L"in pas or "M"in pas or "N"in pas or "O"in pas or "P"in pas or "Q"in pas or "R"in pas or "S"in pas or "T"in pas or "U"in pas or "V"in pas or "W"in pas or "X"in pas or "Y"in pas  or "Z"in pas):
       if ("a"in pas or"b"in pas or"c"in pas or"d"in pas or"e"in pas or"f"in pas or "g"in pas or"h"in pas or"i"in pas or"j"in pas or"k"in pas or"l"in pas or"m"in pas or"n"in pas or"o"in pas or"p"in pas or"q"in pas or"r"in pas or"s"in pas or"t"in pas or"u"in pas or"v"in pas or"w"in pas in pas or"x"in pas or"y"in pas or"z"in pas):
           if "@"in pas  or "#"in pas or "$"in pas  or "!"in pas:
               if ("1"in pas  or "2"in pas  or "3"in pas  or "4"in pas  or "5"in pas  or "6"in pas  or "7"in pas  or "8"in pas or"9"in pas or"0"in pas):
                   print("correct and strong password")
               else:
                   print("number is missing so enter number")
           else:
               print(" special charactor is missing so enter special character")
       else:
           print("small charactor is missing so enter small charactor")           
   else:
       print("capital charactor is missing so enter the capital latter ")
else:
   print("please enter minimum 8 charactor)


