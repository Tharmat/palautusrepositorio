from matchers import All, And, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.query = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))
    
    def build(self):
        return self.query