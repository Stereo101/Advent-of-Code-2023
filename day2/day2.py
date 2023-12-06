from advent import Session
import math

aoc = Session(2023,2)

def game_id(game):
    return int(game.split(": ")[0].split(" ")[1])

def maxes(game):
    d = {"red":0,"blue":0,"green":0}
    for iteration in game.split(": ")[1].split("; "):
        for move in iteration.split(", "):
            n,color = move.split(" ")
            d[color] = max(d[color],int(n))
    return [d["red"],d["green"],d["blue"]]

with aoc.fp() as f:
    games = [line.strip() for line in f.readlines()]

limits = [12,13,14]

silver = sum(game_id(game) for game in games if all(a <= b for a,b in zip(maxes(game),limits)))
gold = sum(math.prod(maxes(game)) for game in games)

aoc.solution(1,silver)
aoc.solution(2,gold)
