from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    TYPES_CARS = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: [User] = []
        self.vehicles: [BaseVehicle, CargoVan, PassengerCar] = []
        self.routes: [Route] = []
        self.cur_id = 0

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        else:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.TYPES_CARS:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for c in self.vehicles:
            if c.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.TYPES_CARS[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif r.start_point == start_point and r.end_point == end_point and r.length > length:
                r.is_locked = True
                self.cur_id += 1
                self.routes.append(Route(start_point, end_point, length, self.cur_id))
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

        else:
            self.cur_id += 1
            self.routes.append(Route(start_point, end_point, length, self.cur_id))
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):

        user = ""
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                if u.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

                user = u
                break

        vehicle = ""
        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                if v.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

                vehicle = v
                break

        route = ""
        for r in self.routes:
            if r.route_id == route_id:
                if r.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                route = r
                break

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()

        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles = list(filter(lambda x: x.is_damaged, self.vehicles))
        vehicles = list(sorted(vehicles, key=lambda x: (x.brand, x.model)))

        for ind in range(count):
            if ind == len(vehicles):
                break
            v = vehicles[ind]
            v.change_status()
            v.battery_level = 100

        return f"{len(vehicles) if vehicles else 0} vehicles were successfully repaired!"

    def users_report(self):
        sorted_user = list(sorted(self.users, key=lambda x: x.rating, reverse=True))

        result = []
        for u in sorted_user:
            result.append(str(u))

        result = "\n".join(result)
        return f"*** E-Drive-Rent ***\n{result}"


app = ManagingApp()
print(app.register_user('Tisha', 'Reenie', '7246506'))
print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user('Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
