from process_input import get_input, question


def minimum_presses():
    questions = get_input()
    total = 0
    for q in questions:
        delta = ((q.xA * q.yPrize) - (q.yA * q.xPrize)) / (
            (q.xA * q.yB) - (q.yA * q.xB)
        )

        lamb = ((q.xPrize) - (q.xB * delta)) / (q.xA)
        if delta % 1 != 0 or lamb % 1 != 0:
            continue
        else:
            total += (lamb * 3) + (delta)
    print(total)


minimum_presses()
