
from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn


class QueryBuilder():
    def __init__(self):
        self._matchers = []
    
    def add_matcher(self, matcher):
        self._matchers.append(matcher)
    
    def playsIn(self,team):
        self.add_matcher(PlaysIn(team))
        return self
    
    def hasAtLeast(self, argument, attribute):
        self.add_matcher(HasAtLeast(argument, attribute))
        return self

    def hasFewerThan(self, argument, attribute):
        self.add_matcher(HasFewerThan(argument, attribute))
        return self

    def build(self):
        return All(*self._matchers)