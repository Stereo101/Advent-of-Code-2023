from advent import Session

aoc = Session(2023,1)
silver = None
gold = None

def digit_filter(s):
    return "".join(c for c in s if c in "123456789")

def text_digit_filter(s):
    replacements = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    
    digits = []
    for i in range(len(s)):
        if s[i] in "123456789":
            digits.append(s[i])
            continue
        for look_back in range(3,5+1):
            if i < look_back-1:
                break
            seq = s[i-(look_back-1):i+1]
            if(seq in replacements):
                digits.append(replacements[seq])
    
    return "".join(digits)

def calibration(digits):
    return int(digits[0]+digits[-1])

with aoc.fp() as f:
    lines = [line for line in f.readlines()]
    
silver = sum(calibration(digit_filter(line)) for line in lines)
gold = sum(calibration(text_digit_filter(line)) for line in lines)

aoc.solution(1,silver)
aoc.solution(2,gold)
