import random
import  time

def basic_atk(player):
    if random.randint(1, 100) <= player.cri_luk:
        damage = player.attack * 2
        print(f"치명타!! 데미지 : {damage}\n")
    else:
        damage = player.attack
        print(f"기본 공격!! 데미지 : {damage}\n")
    return  damage

def skill_ack(player):
    print("\n[스킬]")
    for idx, skill in enumerate(player.skill):
        print(f"{idx + 1}. {skill["name"]} (MP소모: {skill["mp_cost"]}, 데미지 배수: {skill["damage_multiple"]})")

    skill_choice = int(input("사용할 스킬을 선택해주세요:")) - 1

    if 0 <= skill_choice < len(player.skill):
        skill = player.skill[skill_choice]
        if player.mp >= skill["mp_cost"]:
            player.mp -= skill["mp_cost"]
            damage = int(player.attack * skill["damage_mulitple"])
            print(f"\n{player.nickmane}가 {skill["name"]}을 시전하였습니다. {damage}\n")
            return damage
        else:
            print("MP가 부족합니다. 기본 공격을 수행합니다.")
            return basic_atk(player)
    else:
        print("잘못된 선택입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)

def player_turn(player):
    print("\n행동을 선택하세요.")
    print("1. 기본 공격")
    print("2. 스킬 공격")
    action = input("선택:")

    if action == "1":
        return basic_atk(player)
    elif action == "2":
        return skill_ack(player)
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다.")
        return basic_atk(player)



def battle(player, monster):
    print(f"{player.nickmane} vs {monster.name}")
    while player.hp >0 and monster.hp > 0:
        print("\n==========================================================")
        print(f"{player.nickmane} [HP: {player.hp}, MP: {player.mp}]")
        print(f"{monster.name} [HP: {monster.hp}]")

        #플레이어 턴
        damage = player_turn(player)
        monster.hp -= damage

        time.sleep(2)

        #플레이어가 몬스터를 때려잡은 경우
        if monster.hp <= 0:
            print(f"{monster.name}을/를 처치했습니다.")
            #배틀 보상

            #몬스터의 데이터와 플레이어의 데이터 초기화
            monster.hp = monster.max_hp
            player.hp = player.max_hp
            player.mp = player.max.mp
            break
        #몬스터 턴
        player.hp -= monster.attack
        print(f"{monster.name}의 반격! {monster.attack} 데미지!")

        time.sleep(2)

        #플레이어가 몬스터에게 패배한 경우
        if player.hp <= 0:
            print("패배했습니다. 게임 오버!")
            #플레이가 소지하고 있던 아이템을 초기화
            break


        #마나 회복 시스템