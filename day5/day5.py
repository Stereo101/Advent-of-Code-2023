from advent import Session

aoc = Session(2023,5)

with aoc.fp() as f:
    seeds,*maps = f.read().split("\n\n")
    seeds = [int(s) for s in seeds.split(": ")[1].split()]

map_ranges = []
for m in maps:
    ranges = []
    for line in m.strip().split("\n")[1:]:
        ranges.append([int(x) for x in line.strip().split()])
    ranges.sort(key=lambda x: x[1])
    map_ranges.append(ranges)
    
def resolve(e,mapping):
    for i in range(len(mapping)):
        (dest,source,r) = mapping[i]
        if e >= source and e < source+r:
            dist_to_next = float("INF")
            if(i+1 < len(mapping)):
                _,next_source,_ = mapping[i+1]
                dist_to_next = next_source-e
            return dest+e-source,dist_to_next
    return e,float("INF")

silver = float("INF")
for s in seeds:
    v = s
    for mr in map_ranges:
        v,_ = resolve(v,mr)
    silver = min(silver,v)
    
gold = float("INF")
for pair_index in range(len(seeds)//2):
    offset = pair_index*2
    start,r = seeds[offset],seeds[offset+1]
    s = start
    while s < start+r:
        next_dist = float("INF")
        v = s
        for mr in map_ranges:
            v,dist = resolve(v,mr)
            next_dist = min(next_dist,dist)
        gold = min(gold,v)
        s += next_dist

aoc.solution(1,silver)
aoc.solution(2,gold)
