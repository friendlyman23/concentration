import concentration_constants as CC

publicBoard = [
    ([
        ' _____ ' for _ in range(CC.CARDS_PER_ROW)
    ],
    [
        '|     |' for _ in range(CC.CARDS_PER_ROW)
    ],
    [
        '|CARD |' for _ in range(CC.CARDS_PER_ROW)
    ],
    [
        f'|   {x*i} |' if x * i < 10 else f'|  {x*i} |' for x in range(1, CC.CARDS_PER_ROW + 1)
    ],
    [
        '|_____|' for _ in range(CC.CARDS_PER_ROW)
    ])
    for i in range(CC.CARD_ROWS)
]
