from advent import Session

aoc = Session(2023,4)
silver = None
gold = None

with aoc.fp() as f:
    lines = [line.strip() for line in f.readlines()]
    
cards = []
for line in lines:
    card_id = int(line.split(": ")[0].strip().split()[1])
    winning_text,have_text = line.split(":")[1].strip().split(" | ")
    winning = set(int(x) for x in winning_text.strip().split())
    have = set(int(x) for x in have_text.strip().split())
    cards.append((card_id,winning,have))

silver = sum(2**(len(winning & have)-1) for (_,winning,have) in cards if len(winning & have) != 0)

processed = [0]*len(cards)
card_count = [1]*len(cards)
empty = False
while not empty:
    empty = True
    for i in range(len(cards)):
        if card_count[i] != 0:
            empty = False
        else:
            continue
        (card_id,winning,have) = cards[i]
        score = len(winning & have)
        for k in range(i+1,i+1+score):
            card_count[k] += card_count[i]
        processed[i] += card_count[i]
        card_count[i] = 0
gold = sum(processed)

aoc.solution(1,silver)
aoc.solution(2,gold)