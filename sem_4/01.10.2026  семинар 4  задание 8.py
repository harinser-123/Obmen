def choose_bait(baits, reach):
    best_index = -1
    best_attractiveness = None
    for i, bait in enumerate(baits):
        distance, attractiveness = bait
        if distance <= reach:
            if best_index == -1 or attractiveness > best_attractiveness:
                best_index = i
                best_attractiveness = attractiveness
    return best_index
