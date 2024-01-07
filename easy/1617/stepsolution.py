import sys
input_string = sys.argv[1]
input_string = input_string.upper()
# dominoes in a line, each dominoe is represented by a char, L, R, or .
# simple method takes O(n^2) time and O(1) extra space
# Example Output: 
# Step<0>   ..LR.......L..R..... -> .LLRR.....LL..RR....  True
# Step<1>   .LLRR.....LL..RR.... -> LLLRRR...LLL..RRR...  True
# Step<2>   LLLRRR...LLL..RRR... -> LLLRRRR.LLLL..RRRR..  True
# Step<3>   LLLRRRR.LLLL..RRRR.. -> LLLRRRR.LLLL..RRRRR.  True
# Step<4>   LLLRRRR.LLLL..RRRRR. -> LLLRRRR.LLLL..RRRRRR  True
# Step<5>   LLLRRRR.LLLL..RRRRRR -> LLLRRRR.LLLL..RRRRRR  False

modified = True
step = 0
while(modified):
    sb = f"Step<{step}>";
    sb = sb.ljust(10)
    sb+= input_string
    input_string = [c for c in input_string] # str doesn't support item assignment
    i = 0
    modified = False
    while(i<len(input_string)):
        if(input_string[i]!='.'):
            pass
        elif((i>=0 and input_string[i-1]=="R") and (i<len(input_string)-1 and input_string[i+1]=="L")):
            pass
        elif(i>0 and input_string[i-1]=="R"):
            input_string[i] = "R"
            i+=1
            modified = True
        elif(i<len(input_string)-1 and input_string[i+1]=="L"):
            input_string[i] = "L"
            modified = True
        i+=1
    input_string = "".join(input_string)
    sb+=" -> "+input_string+"  "+str(modified)
    print(sb)
    step+=1

sys.exit(0)
