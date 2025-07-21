class Player:
    def __init__(self, nickname, level=1, gold=0, attack=10, exp=0, max_exp=100, hp=100, max_hp=100, mp=50, max_mp=50, cri_luk=0, skills=None, items=None):
        self.nickname = nickname
        self.level = level
        self.gold = gold
        self.attack = attack
        self.exp = exp
        self.max_exp = max_exp
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.cri_luk = cri_luk
        self.skills = skills if skills else [
            {"name": "달팽이 세마리", "mp_cost": 10, "damage_multiple": 1.2},
            {"name": "달팽이 네마리", "mp_cost": 18, "damage_multiple": 1.5},
            {"name": "달팽이 다섯마리", "mp_cost": 23, "damage_multiple": 1.8}
        ]
        self.items = items if items else []

    def to_dict(self):
        return self.__dict__#클래스(인스턴스)의 내부 상태를 딕셔너리로 변환

    @classmethod
    def from_dict(cls, data):
        player = cls(**data)
        return player
    """
    cls(클래스 자신)를 인자로 받아, data 딕셔너리의 키-값 쌍을 생성자의 키워드 인자로 사용하여 새로운 객체를
    생성하고 반환하는 역할
    딕셔너리 앞에 **가 붙게 되면 언패킹이 됨
    즉 자기 자신의 클래스의 객체 생성자에 가져온 딕셔너리 데이터를 언패킹하여 각 속성에 초기화 하게 됨
    """
    """
    인스턴스 메소드 => 우리가 기본적으로 알고 있는 메소드
    스태틱 메소드 => 클래스 내에 유틸성 메소드, 즉 인스턴스나 클래스의 속성에 접근할 수 없음
    클래스 메소드 => 인스턴스를 생성하지 않고 클래스에 직접적으로 접근함
    """

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.max_exp:
            left_amount = self.exp - self.max_exp
            self.exp = 0
            self.level_up(left_amount)

    def level_up(self, amount):
        self.level += 1
        self.attack += 5
        self.max_exp += 10
        self.max_hp += 10
        self.max_mp =+ 10
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp += amount
        self.max_exp =int(self.max_exp * 1.5)
        print(f"레벨업! {self.level}레벨이 되었습니다! \n공격력 +5\n 최대 HP +10\n최대 MP + 10")

class Monster:
    def __init__(self, name, max_hp, attack, exp_reward, gold_reward):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward