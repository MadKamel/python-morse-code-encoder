import time
# this table holds morse data
#   . = wait one unit of time
#   0 = dot
#   1 = dash
#
# morse chars
#   A-Z (you know these)
#   0-9 (these too)
#   _   (space between words)
#   -   (space between letters)
#
morseDefTable = {
"_"    : "......",      # onto new word (7 waits)
"-"     : "..",         # onto new letter (3 waits)
"A"     : "0.1.",       # i put _ down as 6 waits and - as 2 because
"B"     : "1.0.0.0.",   #   when it's outputted, the letter immediately
"C"     : "1.0.1.0.",   #   after already has a dot there. if i put it
"D"     : "1.0.0.",     #   down as 7 or 3 waits, it'd end up being
"E"     : "0.",         #   8 or 4 in practice.
"F"     : "0.0.1.0.",
"G"     : "1.1.0.",     # ex.
"H"     : "0.0.0.0.",   #   0.1...0.1.......0.1.
"I"     : "0.0.",       #
"J"     : "0.1.1.1.",   # this is the correct way to do it.
"K"     : "1.0.1.",
"L"     : "0.1.0.0.",
"M"     : "1.1.",
"N"     : "1.0.",
"O"     : "1.1.1.",
"P"     : "0.1.1.0.",
"Q"     : "1.1.0.1.",
"R"     : "0.1.0.",
"S"     : "0.0.0.",
"T"     : "1.",
"U"     : "0.0.1.",
"V"     : "0.0.0.1.",
"W"     : "0.1.1.",
"X"     : "1.0.0.1.",
"Y"     : "1.0.1.1",
"Z"     : "1.1.0.0.",
"0"     : "0.1.1.1.1.",
"1"     : "0.0.1.1.1.",
"2"     : "0.0.0.1.1.",
"3"     : "0.0.0.0.1.",
"4"     : "0.0.0.0.0.",
"5"     : "1.0.0.0.0.",
"6"     : "1.1.0.0.0.",
"7"     : "1.1.1.0.0.",
"8"     : "1.1.1.1.0.",
"9"     : "1.1.1.1.1."}

def toMorse(txt):
    output = ""
    for i in range(len(txt)):
        output = output + morseDefTable[txt[i]]
    return output

def formatMMsg(txt):
    output = ""
    for i in range(len(txt)):
        if not txt[i] == " ":
            output = output + txt[i].upper()
            if i == len(txt)-1:                 # i honestly don't know how this works
                pass                            # i'm sorry
            elif not txt[i+1] == " ":
                output = output + "-"
        else:
            output = output + "_"
    return output

def fromMorse(morse):
    for i in range(morse):
        #listen to stream
        pass

def playMorse(msg, de):
    for i in range(len(msg)):
        if msg[i] == ".":
            print(".")
        elif msg[i] == "0":
            print("Dot!")
        elif msg[i] == "1":
            print("Dash!")
            time.sleep(de*2)
        time.sleep(de)



# remember, syntax is as follows:
#   "C-Q" is CQ                         (the dash is a space between letters)
#   "S-P-A-C-E_T-H-I-S" is SPACE THIS   (the underscore is a space)
#
while True:
    morse = toMorse(formatMMsg(input()))
    print(morse + "\n")
    playMorse(morse, 0.05)
