def find_last(s,t):
    last_pos = -1
    while True:
        pos = s.find(t, last_pos + 1)
        if pos == -1:
            return last_pos
        else:
            last_pos = pos

print(find_last('bbbbbbbbbbb', 'b'))
