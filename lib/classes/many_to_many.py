class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, '_name'):
            self._name = value

    def trips(self):
        return [value for value in Trip.all if value.national_park.name == self.name]
    
    def visitors(self):
        return list({value.visitor for value in Trip.all if value.national_park.name == self.name})
    
    def total_visits(self):
        return sum(1 for value in Trip.all if self.name == value.national_park.name)
    
    def best_visitor(self):
        visitor_counts = {}
        for value in Trip.all:
            if value.national_park == self:
                visitor_counts[value.visitor] = visitor_counts.get(value.visitor, 0) + 1

        if not visitor_counts:
            return None

        return max(visitor_counts, key=visitor_counts.get)


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        self._national_park = value

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and (len(value) >= 1 and len(value) <= 15):
            self._name = value

    def trips(self):
        return [value for value in Trip.all if self.name == value.visitor.name]
    
    def national_parks(self):
        return list({value.national_park for value in Trip.all if value.visitor.name == self.name})
    
    def total_visits_at_park(self, park):
        return sum(1 for value in Trip.all if value.national_park.name == park.name)