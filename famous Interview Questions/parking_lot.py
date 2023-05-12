""" 
    Functional requirements:
        - parking space can have multiple terminals
        - each terminal can have single entry/exit
        - different types of parking space (motor cycle, LWV, HWV)
        - pay on hour basis
        - capacity ~30k
        - payment methods acceptance
        - monitoring

    Components Break Down:
        - Parking lot system
        - Terminal
            ~ Payment system at exit
            ~ Ticket generation at entry
            ~ Should guide to nearest parking spot at the time of entry.
        - Parking Spot 
        - Database
"""


from abc import abstractmethod
import datetime


class PaymentInterface:
    def __init__(self) -> None:
        pass


class UPIPayment(PaymentInterface):
    pass


class CreditCardPayment(PaymentInterface):
    pass


class AbstractParkingType:
    def __init__(self) -> None:
        self.is_available: bool = True

    @abstractmethod
    def reserve(self):
        raise NotImplementedError

    @abstractmethod
    def toggle_avaibility(self) -> bool:
        self.is_available = ~self.is_available


class MotorCycleParkingType(AbstractParkingType):
    def get_parking_rate(self) -> int:
        return 10

    def reserve():
        pass


class CarParkingType(AbstractParkingType):
    def get_parking_rate(self) -> int:
        return 30

    def reserve():
        pass


class ParkingTicket:
    def __init__(self) -> None:
        self.parking_spot: AbstractParkingType = None
        self.check_in = None
        self.check_out = None


class Terminal:
    def __init__(self) -> None:
        self.parking_spots = []
        self.available_parking_spots = []
        self.occupied_parking_spots = []

    def entry(self, parking_type: str):
        # get nearest parking spot available (based on type)
            # manage heap, heap.pop and heapify()
        parking_spot = CarParkingType()
        parking_spot.toggle_avaibility()
        ticket = ParkingTicket()
        ticket.parking_spot = parking_spot
        ticket.check_in = datetime.datetime.now()
        self.occupied_parking_spots.append(parking_spot)

    def exit(self, parking_ticket: ParkingTicket):
        # insert latest parking spot in the heap and perform heapify
        parking_ticket.check_out = datetime.datetime.now()
        parking_ticket.parking_spot.toggle_avaibility()
        # rate calculation and payment 
        self.available_parking_spots.append(parking_ticket.parking_spot)


class Parking:
    def __init__(self) -> None:
        pass
