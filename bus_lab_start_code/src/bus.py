class Bus:
    def __init__(self, route_number, destination):

        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        print(self.passengers)

    def drive(self):
        return ("Brum brum")

    def passenger_count(self):
        # print(self.passengers)
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

