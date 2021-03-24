from enum import Enum

def entity_factory(classname):
     cls = globals()[Challenge.fromName(classname)]
     return cls

class Challenge(bytes, Enum):

    def __new__(cls, value, label, entity):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.entity = entity
        return obj

    def __repr__(self):
        return "<Challenge label:%s >" % (self.label)

    def __str__(self):
        return "label:%s" % (self.label)

    HELP     = (0,  'help', 'Help')
    SOCKS    = (1,  'socks', 'SockMerchant')

    @classmethod
    def fromName(cls, name):
        for ch in Challenge:
            if name == ch.label:
                return ch.entity

        return Challenge.HELP.entity

class SockMerchant():
    def __init__(self, sockData):
        self.fields = {}

        self.fields['pile'] = sockData.pop(0)
        self.fields['colors'] = sockData

    def __repr__(self):
        return "<Sock data:%s>" % (sockData)

    def __str__(self):
        return "SockMerchant:%s" % (self.fields['colors'])

    def evaluate(self):
        result = 0
        n = self.fields['pile']
        ar = self.fields['colors']
        if 1 < n <= 100 and len(ar) == n:
            counts = dict()
            for color in [c for c in ar if 1 <= c <= 100]:
            # for color in ar:
              counts[color] = counts.get(color, 0) + 1
              if counts[color] == 2:
                  result += 1
                  counts[color] = 0

        # result = len([x for x in counts if x == probe])
        print("sockMerchant: %s" % (result))
        # print("sockMerchant: n: %s ar: %s r: %s" % (n, ar, result))
        return result
