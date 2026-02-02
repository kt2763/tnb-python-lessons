class Party:
    """パーティークラス"""

    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def __getitem__(self, index):
        """party[0]のようにアクセス"""
        return self.members[index]

    def __setitem__(self, index, value):
        """party[0] = "戦士"のように代入"""
        self.members[index] = value

    def __len__(self):
        return len(self.members)


# 使用例
party = Party()
party.add_member("勇者")
party.add_member("魔法使い")
party.add_member("僧侶")

print(party[0])  # 勇者
print(party[1])  # 魔法使い

party[1] = "賢者"  # 魔法使いを賢者に変更
print(party[1])  # 賢者

# forループでも使える!
for member in party:
    print(member)
