from typing import List, Dict

class Garage:
    """A class to represent a garage with a limited capacity for cars."""
    def __init__(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.cars: List[str] = []
        self.capacity = capacity

    def add_car(self, car: str):
        """Adds a car to the garage if there is space."""
        if self.get_car_count() == self.capacity:
            raise OverflowError("Garage is full, cannot add more cars")
        self.cars.append(car)

    def get_car_count(self) -> int:
        """Returns the number of cars currently in the garage."""
        return len(self.cars)

    def get_cars(self) -> List[str]:
        """Returns a list of all cars in the garage."""
        return self.cars

    def get_total_value(self, price_list: Dict[str, float]) -> float:
        """Calculates the total value of all cars in the garage."""
        total_value = 0.0
        for car in self.cars:
            total_value += price_list.get(car, 0.0)
        return total_value