bullet_price = int(input())                     # [0-100]
chambers = int(input())                         # [1-5000]
bullets = [int(x) for x in input().split()]    # [1-100]
locks = [int(x) for x in input().split()]       # [1-100]
intelligence_value = int(input())               # [1-100000]
num_of_bullets = len(bullets)


fired_shots = 0
chambers_with_bullets = chambers
while bullets:
    fired_shots += 1
    chambers_with_bullets -= 1

    if bullets[-1] > locks[0]:
        bullets.remove(bullets[-1])
        print("Ping!")
    else:
        bullets.remove(bullets[-1])
        print("Bang!")
        locks.remove(locks[0])
        if len(locks) == 0:
            left_bullets = num_of_bullets - fired_shots
            earnings = intelligence_value - (fired_shots * bullet_price)
            # --------------
            if chambers_with_bullets == 0:
                if num_of_bullets != fired_shots:
                    print("Reloading!")
            # --------------
            print(f"{left_bullets} bullets left. Earned ${earnings}")
            break
    #--------------
    if chambers_with_bullets == 0:
        if num_of_bullets != fired_shots:
            print("Reloading!")
            chambers_with_bullets = chambers
    # --------------
if locks:
    print(f"Couldn{chr(39)}t get through. Locks left: {len(locks)}")
