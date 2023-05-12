""" Adapter pattern lives here."""

class AdapterPinSocket:
    def charge(self):
        print("Charging with adapter connected to wall started")


class AdapterInterface:
    def transform(self):
        pass


class Adapter(AdapterInterface):
    def __init__(self, pin: AdapterPinSocket) -> None:
        self.pin = pin

    def transform(self):
        self.pin.charge()

class LaptopChargerSocket:
    def __init__(self, adapter: AdapterInterface) -> None:
        self.adapter = adapter

    def charge(self):
        self.adapter.transform()


adapter_pin: AdapterPinSocket = AdapterPinSocket()
adapter: Adapter = Adapter(pin=adapter_pin)
laptop_charger: LaptopChargerSocket = LaptopChargerSocket(adapter=adapter)
laptop_charger.charge()


# https://refactoring.guru/design-patterns/adapter/python/example#:~:text=Adapter%20is%20a%20structural%20design,recognizable%20by%20the%20second%20object.
class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)