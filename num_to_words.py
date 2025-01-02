i_to_s = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

i_to_s_tens = {
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety",
}

def read3(x):
    firstwo = x % 100
    last = x // 100

    ans = ""
    if last != 0:
        ans+= i_to_s[last] + " hundred "

    if firstwo <20:
        ans+= i_to_s[firstwo]
    else:
        ans+= i_to_s_tens[firstwo//10] + " " + i_to_s[firstwo%10]

    return ans


places = ["","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion"]

def readnum(x:int,buf=0) -> str:
    if x == 0 and buf > 0:
        return ""
    elif x==0 and buf == 0:
        return " zero"
    return readnum(x//1000,buf+1) + " " + read3(x%1000) + " " + places[buf]

while True:
    print(readnum(int(input())))