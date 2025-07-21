import os
from package.models import Player
from package.utils import save_game, load_game
from package.constants import monsters
from package.game import battle


def main():
    print("턴제 RPG 게임")
    if os.path.exists("save.json"):
        choice = input("1. 기존 캐릭터 불러오기\n2. 새로 시작하기\n선택:")
        if choice == "1":
            player = load_game() #load_game에 대한 반환값이 player 객체
            if not player:
                print("저장된 캐릭터가 없습니다.")
                nickname = input("닉네임을 입력해 주세요 : ")
                player = Player(nickname)
        elif choice == "2":
            nickname = input("닉네임을 입력해 주세요 : ")
            player = Player(nickname)
    else:
        nickname = input("닉네임을 입력해 주세요 : ")
        player = Player(nickname)

    while True:
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("메뉴 선택 : ")

        if choice == "1":
            print("\n[배틀]")
            #싸울 몬스터 선택
            for idx, monster in enumerate(monsters):
                print(f"{idx + 1}. {monster.name} (HP : {monster.hp}, 공격력: {monster.attack}")
            m_choice = int(input("몬스터를 선택하세요 :")) - 1
            if 0 <= m_choice < len(monsters):
                battle(player, monsters[m_choice])

            else:
                print("잘못된 입력입니다.")
        elif choice == "2":
            print("\n[상점]")
        elif choice == "3":
            print("\n[내 아이템 확인]")
        elif choice == "4":
            print("\n[내 정보 확인]")
            print(f"닉네임: {player.nickname}\n레벨: {player.level} ({player.exp}/{player.max_exp})\n공격력: {player.attack}\n치명타 확률: {player.cri_luk}%\nHP: {player.hp}\nMP: {player.mp}\n골드: {player.gold}")
        elif choice == "5":
            print("\n[게임 종료]")
            save_game(player)
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
#이 파이썬 파일이 직접 실행되고 여기가 본체로 돌아가게 하기 위해