

class Effect:
    def __init__(self, text: str, mag: int):
        self.mag = mag
        self.__text = text
    @property
    def mag(self):
        return self.__mag
    @mag.setter
    def mag(self, val):
        self.__mag = val
    @property
    def text(self):
        return self.__text

    def __str__(self):
        return str(self)

class Spell:
    '''implement spell
    >>> s =Spell()
    >>> s.add_effect(Effect('restore health', 40))
    >>> print(s)
    Spell: restore health @ 40, $40
    >>> s.add_effect(Effect('cure poison', 20))
    >>> print(s)
    Spell: restore health @ 40 + cure poison @ 20, $120
    >>>s.add_effect(Effect('restore health',10))
    >>> print(s)
    Spell: restore health @ 40 + cure poison @ 20 + restore health @10, $140
    '''

    def __init__(self):
        self.__spell = []
        self.__value = 0

    def add_effect(self,effect: Effect):
        if effect not in self.__spell:
            self.__spell.append(effect)

    def change_effect_magnitude(self,index: int, newmag: int):
        if index >= len(self.__spell):
            raise IndexError
        if newmag <= 0:
            raise ValueError
        for i in range(len(self.__spell)-1):
            if i == index:
                self.__spell[i].mag = newmag

    @property
    def _spell(self):
        return self.__spell
    @property
    def value(self):
        temp = []
        for effect in self.__spell:
            temp.append(effect.mag)
        val = len(self.__spell)* sum(temp)
        return val

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        concat = ''
        for effect in self.__spell:
            concat += effect.text + ' @ ' + str(effect.mag) + ' + '
        concat = concat.rstrip(' + ')
        return f'Spell: {concat}, ${self.value}'


class AreaSpell(Spell):
    '''Implement an area spell=
    >>> e1 = Effect('buff def', 20)
    >>> e2 = Effect('buff afk', 10)
    >>> s1 = Spell()
    >>> s1.add_effect(e1)
    >>> s1.add_effect(e2)
    >>> print(s1)
    Spell: buff def @ 20 + buff atk @ 10, $60
    >>> print(s1)
    Spell: buff def @ 20 + buff atk @ 10, $418
    '''
    def __init__(self,radius):
        super().__init__()
        if radius > 0:
            self.radius = radius

    @property
    def value(self):
        return round(self.value*((self.radius +1)**1.4))




#
# s1 = Effect('ji',3)
# s =Spell()
# s.add_effect(Effect('restore health', 40))
# print(s)
# s.add_effect(Effect('cure poison', 20))
# print(s)



#inheritance
e1 = Effect('buff def', 20)
e2 = Effect('buff afk', 10)
s1 = Spell()
s1.add_effect(e1)
s1.add_effect(e2)
s2 = AreaSpell(3)
s2.add_effect(e1)
s2.add_effect(e2)
print(s1)
print(s2)
# p =Spell()
# p.add_effect(Effect('restore health', 40))
# p.add_effect(Effect('cure poison', 20))
# print(s == p)
# s.change_effect_magnitude(0, 99)
# print(s)
