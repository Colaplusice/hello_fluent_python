#encoding=utf-8
import collections
from random import choice
Card=collections.namedtuple('Card',['rank','suit'])
class FremchDeck:
    #card number
    ranks=[str(n) for n in range(2,11)+list('JQKA')]

    #花色
    suits='spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    #重写get 方法
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':

    beer_card=Card('7','diamonds')
    print(beer_card)

    deck=FremchDeck()
    print(len(deck))
    print(deck[-1])

    # 随机取一张牌
    ras=choice(deck)
    print(ras)

    # 找出4张deck 每隔13张找一张

    sd=deck[12::13]
    print(sd)
        #迭代输出
    for card in reversed(deck):
        print(card)