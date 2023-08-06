import time
import random

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def __str__(self):
        return f"Vehicle {self.vehicle_id}"

class TrafficSignal: 
    def __init__(self, signal_id):
        self.signal_id = signal_id
        self.green = True

    def __str__(self):
        return f"Traffic Signal {self.signal_id}"

    def set_green(self):
        self.green = True

    def set_red(self):
        self.green = False

class Road:
    def __init__(self, road_id, signals):
        self.road_id = road_id
        self.signals = signals

    def add_signal(self, signal):
        self.signals.append(signal)

    def wait(self, vehicle):
        print(f"{vehicle} is waiting at Road {self.road_id}")
        time.sleep(random.randint(1, 5))

    def move(self, vehicle):
        print(f"{vehicle} is moving at Road {self.road_id}")
        time.sleep(random.randint(1, 3))

    
def traffic_simulation():
    signals = [TrafficSignal(1), TrafficSignal(2)]
    road1 = Road(101, [signals[0]])
    road2 = Road(102, [signals[1]])

    vehicles = [Vehicle(i + 1) for i in range(5)]

    while True:
        for signal in signals:
            signal.set_green()
            print(f"{signal} is green")
            for vehicle in vehicles:
                if random.random() < 0.5:
                    road1.wait(vehicle)
                else:
                    road2.wait(vehicle)
            signal.set_red()
            print(f'{signal} is red')
            time.sleep(1)

        for vehicle in vehicles:
            if signals[0].set_green():
                road1.move(vehicle)
            else:
                road2.move(vehicle)

if __name__ == "__main__":
    traffic_simulation()









