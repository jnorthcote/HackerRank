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
    VALLEYS  = (2,  'valleys', 'CountingValleys')

    @classmethod
    def fromName(cls, name):
        for ch in Challenge:
            if name == ch.label:
                return ch.entity

        return Challenge.HELP.entity

class SockMerchant():
    def __init__(self, pile, sockData):
        self.fields = {}

        self.fields['pile'] = pile
        self.fields['colors'] = sockData

    def __repr__(self):
        return "<Sock data:%s>" % (sockData)

    def __str__(self):
        return "SockMerchant:%s" % (self.fields['colors'])

    def evaluate(self):
        result = 0
        n = self.fields['pile']
        ar = self.fields['colors']
        print("SockMerchant.evaluate: n: %s ar: %s" % (n, ar))
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
        return result

class CountingValleys():
    def __init__(self, steps, path):
        self.fields = {}

        self.fields['steps'] = steps
        self.fields['path'] = path

    def __repr__(self):
        return "<path:%s>" % (path)

    def __str__(self):
        return "CountingValleys:%s" % (self.fields['path'])

    def evaluate(self):
        valleys = 0
        steps = self.fields['steps']
        path = self.fields['path']
        if 2 <= steps <= 10**6 and len(path) == steps:
            altitude = 0
            for step in path:
                altitude += 1 if step == 'U' else -1
                print("alt: %s step: %s" % (altitude, step))
                if altitude == 0 and step == 'U':
                    valleys += 1

        print("steps: %s pathlen: %s valleys: %s" % (steps, len(path), valleys))
        return valleys
