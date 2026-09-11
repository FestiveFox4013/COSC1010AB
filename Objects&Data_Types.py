class Car:
    def __init__(self, speed):
        self.speed = speed

    def calculate_distance(self,time):
         return self.speed * time

def main():
    my_car = Car(70)
    hours_list = [6, 10, 15]
    for time in hours_list:
        distance = my_car.calculate_distance(time)
        print(f"Distance traveled in {time} hours: {distance} miles")

if __name__ == "__main__":
    main()