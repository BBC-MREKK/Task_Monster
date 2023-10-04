def min_casts_to_kill_monsters(n, health):
    # Сначала используем заклинание типа 2, пока хотя бы один монстр не умрет
    casts = 0
    while any(health):
        casts += 1
        for i in range(n):
            if health[i] > 0:
                health[i] -= 1

    # Затем используем заклинания типа 1, чтобы нанести оставшийся урон
    for i in range(n):
        casts += health[i]

    return casts

# Чтение количества наборов данных
t = int(input())

# Обработка каждого набора данных
for _ in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    result = min_casts_to_kill_monsters(n, health)
    print(result)