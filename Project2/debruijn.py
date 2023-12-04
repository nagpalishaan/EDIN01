def debruijn2(c, s):
    # s is current state (last 4 symbols)
    # c is coefficients on polynomial

    # Insert [0, 0, 0, 0] into cycle
    if s == [0, 0, 0, 1]:
        return [0, 0, 0, 0]
    elif s == [0, 0, 0, 0]:
        return [1, 0, 0, 0]

    # Compute next state normally
    next_state = 0
    for i in range(4):
        next_state -= c[i] * s[i]

    next_state %= 2
    
    return [next_state, s[0], s[1], s[2]]


def debruijn5(c, s):
    # s is current state (last 4 symbols)
    # c is coefficients on polynomial

    # Insert [0, 0, 0, 0] into cycle
    if s == [0, 0, 0, 1]:
        return [0, 0, 0, 0]
    elif s == [0, 0, 0, 0]:
        return [3, 0, 0, 0]

    # Compute next state normally
    next_state = 0
    for i in range(4):
        next_state -= c[i] * s[i]

    next_state %= 5
    
    return [next_state, s[0], s[1], s[2]]




if __name__ == '__main__':
    # starting states
    state2 = [0, 0, 0, 0]
    state5 = [0, 0, 0, 0]
    debruijn_seq = []
    for k in range(19):
        state2 = debruijn2([0, 0, 1, 1], state2)
        state5 = debruijn5([0, 1, 2, 2], state5)
        print(state2[0])
        # function from Z_2 x Z_5 -> Z_10
        debruijn_seq.append(5 * state2[0] + state5[0])

    # print the 10003 digits on a file called debruijn.txt
    with open('debruijn.txt', 'w') as f:
        for i in range(10003):
            f.write(str(debruijn_seq[i]))
