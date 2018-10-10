# https://app.codesignal.com/company-challenges/mz/eGnd7L4dkkxujHs4Z
def allianceVersusMonster(health_points, attack_damage):
    monster_hp = health_points[0]
    monster_dm = attack_damage[0]
    soldiers_hp = health_points[1:]
    soldiers_dm = attack_damage[1:]

    soldiers = [(soldiers_dm[i], soldiers_hp[i]) for i in range(len(soldiers_hp))]
    # Attack with the most powerful soldier right before its counter-attacked
    # by the monster so it will die. Then try with the second most powerful warrior
    # and so on. Then when all the warriors need only one hit from the monster to
    # die, start again from the most powerful one until the monster is dead, or
    # until all your warriors are dead.
    soldiers = sorted(soldiers)[::-1]
    total = len(soldiers)

    soldier_idx = 0
    # While monster is still alive and we still have soldiers...
    while monster_hp > 0 and soldier_idx < len(soldiers):
        soldier_dm, soldier_hp = soldiers[soldier_idx]
        # Check how many consecutive times can the soldier attack the monster
        # before the soldier is killed.
        if soldier_hp / (monster_dm + 0.0) > 1:
            times = soldier_hp / (monster_dm + 0.0)
            # If divides exactly, attack one time less.
            if times.is_integer():
                times -= 1
            times = int(times)
            monster_damage = times * soldier_dm
            soldier_damage = times * monster_dm
            monster_hp -= monster_damage
            soldiers[soldier_idx] = (soldier_dm, soldier_hp - soldier_damage)
        soldier_idx += 1

    # If after this the monster is still alive, prepare for a last round
    # of attacks.
    soldier_idx = 0
    while monster_hp > 0 and total > 0 and soldier_idx < len(soldiers):
        soldier_dm, soldier_hp = soldiers[soldier_idx]
        # We know this soldier will die for sure so just take damage
        # from the monster in a last attack.
        monster_hp -= soldier_dm
        # Only if the monster is dead then it can counterattack.
        if (monster_hp > 0):
            total -= 1
        soldier_idx += 1

    return total
