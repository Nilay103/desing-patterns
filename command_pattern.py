"""Command pattern example lives here."""

class CommandInterface:
    def execution(self):
        pass

    def undo_execution(self):
        pass


class Invoker:
    def __init__(
        self, 
        light_on: CommandInterface, 
        light_off: CommandInterface, 
        light_dim: CommandInterface, 
        light_bright: CommandInterface
    ) -> None:
        self.light_on = light_on
        self.light_off = light_off
        self.light_dim = light_dim
        self.light_bright = light_bright

    def turn_on_light(self):
        self.light_on.execution()

    def turn_off_light(self):
        self.light_off.execution()
    
    def dim_light(self):
        self.light_dim.execution()

    def bright_light(self):
        self.light_bright.execution()

    
class Reciever:
    def action(self, msg):
        print(f"reciever action {msg} called.")


class LightOnCommand(CommandInterface):
    def __init__(self, reciever: Reciever) -> None:
        self.reciever = reciever

    def execution(self):
        self.reciever.action(msg="on exectuion")

    def undo_execution(self):
        self.reciever.action(msg="undo on execution")
    

class LightBrightnessDimCommand(CommandInterface):
    def __init__(self, reciever: Reciever) -> None:
        self.reciever = reciever

    def execution(self):
        self.reciever.action(msg="dim exectuion")

    def undo_execution(self):
        self.reciever.action(msg="undo dim execution")


class LightOffCommand(CommandInterface):
    def __init__(self, reciever: Reciever) -> None:
        self.reciever = reciever

    def execution(self):
        self.reciever.action(msg="off exectuion")

    def undo_execution(self):
        self.reciever.action(msg="undo off execution")


class LightBrightnessUpCommand(CommandInterface):
    def __init__(self, reciever: Reciever) -> None:
        self.reciever = reciever

    def execution(self):
        self.reciever.action(msg="brightness up exectuion")

    def undo_execution(self):
        self.reciever.action(msg="undo brighness up execution")

light: Reciever = Reciever()
light_on_command: LightOnCommand = LightOnCommand(reciever=light)
light_off_command: LightOffCommand = LightOffCommand(reciever=light)
light_dim_command: LightBrightnessDimCommand = LightBrightnessDimCommand(reciever=light)
light_bright_command: LightBrightnessUpCommand = LightBrightnessUpCommand(reciever=light)
light_remote = Invoker(
    light_on=light_on_command, 
    light_off=light_off_command,
    light_dim=light_dim_command,
    light_bright=light_bright_command,
)

light_remote.turn_on_light()
light_remote.dim_light()
light_remote.bright_light()
light_remote.turn_off_light()
