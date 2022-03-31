import sys 

class Car(object):
    def __init__(self, name, pgood, cost, repair):
        self.name = name
        self.pgood = pgood
        self.pbad = 1 - self.pgood 
        self.cost = cost 
        self.repair = repair

    def eu(self):
        return self.pgood * self.cost + self.pbad * (self.cost + self.repair)

    def __str__(self): return self.name


class CarTest(object):


    def __init__(self, car, pgood_good, pbad_bad, cost):
        self.car = car
        
        self.p_testgood_cargood = pgood_good
        self.p_testbad_cargood = 1 - pgood_good
        self.p_testbad_carbad = pbad_bad
        self.p_testgood_carbad = 1 - pbad_bad

        self.p_testgood = self.p_testgood_cargood * self.car.pgood + self.p_testgood_carbad * self.car.pbad
        self.p_testbad = 1 - self.p_testgood 

        self.p_cargood_testgood = self.p_testgood_cargood * self.car.pgood / self.p_testgood 
        self.p_carbad_testgood = 1 - self.p_cargood_testgood 
        self.p_cargood_testbad = self.p_testbad_cargood * self.car.pgood / self.p_testbad 
        self.p_carbad_testbad = 1 - self.p_cargood_testbad 

        self.cost = cost


    def eu_car_given_outcome(self, car, outcome):
        if car.name == self.car.name:
            if outcome == "+":
                return self.p_cargood_testgood * (self.cost + car.cost) \
                      + self.p_carbad_testgood * (self.cost + car.cost + car.repair)
            else:
                return self.p_cargood_testbad * (self.cost + car.cost) \
                      + self.p_carbad_testbad * (self.cost + car.cost + car.repair)
        else:
            return car.pgood * (self.cost + car.cost) \
                  + car.pbad * (self.cost + car.cost + car.repair)


    def choose(self, outcome, *args):
        # select the car with the minmum cost
        util = sys.maxsize
        car = args[0]
        for c in args:
            cutil = self.eu_car_given_outcome(c, outcome)
            if cutil < util:
                util = cutil 
                car = c
        # I would love some Common Lisp optional args here
        return car, util


    def eu(self, *args):
        return self.p_testgood * self.choose("+", *args)[1] + self.p_testbad * self.choose("-", *args)[1]


c1 = Car("C1", 0.7, -500, 700)
c2 = Car("C2", 0.8, -250, 150)
# can change the price of t1 50 -> 10 to get a different choice
t1 = CarTest(c1, 0.8, 0.65, 50)
t2 = CarTest(c2, 0.75, 0.7, 20)


print("Expected utility of buying C1 given we got a + on T1: {}".format(t1.eu_car_given_outcome(c1, "+")))
print("Expected utility of buying C1 given we got a - on T1: {}".format(t1.eu_car_given_outcome(c1, "-")))
print("Expected utility of buying C2 given we ran T1: {}".format(t1.eu_car_given_outcome(c2, "")))

print("If T1 = +, choose: {}".format(c1.name if t1.eu_car_given_outcome(c1, "+") < t1.eu_car_given_outcome(c2, "") else c2.name))
print("If T1 = -, choose: {}".format(c1.name if t1.eu_car_given_outcome(c1, "-") < t1.eu_car_given_outcome(c2, "") else c2.name))

print("Expected utility of buying C1 given we ran T2: {}".format(t2.eu_car_given_outcome(c1, "")))
print("Expected utility of buying C1 given we got a + on T2: {}".format(t2.eu_car_given_outcome(c2, "+")))
print("Expected utility of buying C2 given we got a - on T2: {}".format(t2.eu_car_given_outcome(c2, "-")))

print("If T2 = +, choose: {}".format(c2.name if t2.eu_car_given_outcome(c2, "+") < t2.eu_car_given_outcome(c1, "") else c1.name))
print("If T2 = -, choose: {}".format(c2.name if t2.eu_car_given_outcome(c2, "-") < t2.eu_car_given_outcome(c1, "") else c1.name))
print("If T2 = -, choose: {} ({})".format(*t2.choose("-", c1, c2)))

print("Expected utility of T1: {}".format(t1.eu(c1, c2)))
print("Expected utility of T2: {}".format(t1.eu(c1, c2)))
print("Expected utility of no test: {}".format(min(c1.eu(), c2.eu())))