from abc import ABC, abstractmethod


class OSFeatures(ABC):
    @abstractmethod
    def get_features(self):
        print("abstract features")


class Execution(ABC):
    @abstractmethod
    def get_execution(self):
        print("abstract execution")


class MacOSFeatures(OSFeatures):
    def get_features(self):
        print("Mac OS Features")


class WindowsOSFeatures(OSFeatures):
    def get_features(self):
        print("Windows OS Features")


class LinuxOSFeatures(OSFeatures):
    def get_features(self):
        print("Linux OS Features")


class MacOSExecution(Execution):
    def get_execution(self):
        print("Mac OS Execution")


class WindowsOSExecution(Execution):
    def get_execution(self):
        print("Windows OS Execution")


class LinuxOSExecution(Execution):
    def get_execution(self):
        print("Linux OS Execution")


class NotificationFactory(ABC):
    @abstractmethod
    def notify(self):
        print("Abstract notification.")


class MacOSNotificationFactory(NotificationFactory):
    def __init__(self, feature: MacOSFeatures, execution: MacOSExecution) -> None:
        self.feature: MacOSFeatures = feature
        self.execution: MacOSExecution = execution

    def notify(self):
        print("Some Mac OS logic")


class WindowsNotificationFactory(NotificationFactory):
    def __init__(self, feature: WindowsOSFeatures, execution: WindowsOSExecution) -> None:
        self.feature: WindowsOSFeatures = feature
        self.execution: WindowsOSExecution = execution

    def notify(self):
        print("Some Windows OS logic")
        

class LinuxOSNotificationFactory(NotificationFactory):
    def __init__(self, feature: LinuxOSFeatures, execution: LinuxOSExecution) -> None:
        self.feature: LinuxOSFeatures = feature
        self.execution: LinuxOSExecution = execution

    def notify(self):
        print("Some Linux OS logic")

mac_feature: MacOSFeatures = MacOSFeatures()
mac_execution: MacOSExecution = MacOSExecution()

MacOSNotificationFactory(mac_feature, mac_execution).notify()
