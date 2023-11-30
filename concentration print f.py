cardNos = []

for i in range(1, 13):
    if i < 10:
        cardNos.append('   ' + str(i) + ' ')
    else:
        cardNos.append('  ' + str(i) + ' ')

cardNos = [cardNos[i:i+4] for i in range(0, 12, 4)]


# for i in range(3):
#     print(' _____ ' * 4)
#     print('|     |' * 4)
#     print('|CARD |' * 4)
#     for k in range(4):
#         print(f'|{cardNos[i][k]}|', end='')
#     print()
#     print('|_____|' * 4)
cardA
for i in range(3):
    for j in range(4):
