class ComputerFactory:
    def __init__(self, monitor, cpu, keyboard_mouse):
        self.monitor = monitor
        self.cpu = cpu
        self.keyboard_mouse = keyboard_mouse

    def com_monitor(self):
        if self.monitor == "1":
            return MacFactory().mac_monitor()
        elif self.monitor == "2":
            return WindowPcFactory().win_monitor()
        else:
            return "You have not selected Monitor"

    def com_cpu(self):
        if self.cpu == "1":
            return MacFactory().mac_cpu()
        elif self.cpu == "2":
            return WindowPcFactory().win_cpu()
        else:
            return "You have not selected CPU"

    def com_keyboard_mouse(self):
        if self.keyboard_mouse == "1":
            return MacFactory().mac_k_m()
        elif self.keyboard_mouse == "2":
            return WindowPcFactory().win_k_m()
        else:
            return "You have not selected keyboard and mouse"


class MacFactory:
    @staticmethod
    def mac_monitor():
        print("Created Mac Monitor")

    @staticmethod
    def mac_cpu():
        print("Created Mac CPU")

    @staticmethod
    def mac_k_m():
        print("Created Mac Keyboard and Mouse")


class WindowPcFactory:

    @staticmethod
    def win_monitor():
        print("Created Window PC monitor")

    @staticmethod
    def win_cpu():
        print("Created Windows PC CPU")

    @staticmethod
    def win_k_m():
        print("Created Windows PC keyboard and Mouse")


def client_request():
    computer_type = input("enter M for Mac, enter W for Windows PC: ").upper()
    if computer_type == "M":
        macmonitor = input("Enter 1 if you want monitor: ")
        maccpu = input("Enter 1 if you want CPU: ")
        mackeyboard_mouse = input("Enter 1 if you want keyboard and mouse: ")
        client = ComputerFactory(macmonitor, maccpu, mackeyboard_mouse)
        client.com_monitor()
        client.com_cpu()
        client.com_keyboard_mouse()

    elif computer_type == "W":
        winmonitor = input("Enter 2 if you want monitor: ")
        wincpu = input("Enter 2 if you want CPU: ")
        winkeyboard_mouse = input("Enter 2 if you want keyboard and mouse: ")
        client = ComputerFactory(winmonitor, wincpu, winkeyboard_mouse)
        client.com_monitor()
        client.com_cpu()
        client.com_keyboard_mouse()
    else:
        print("We only Build Mac and Windows PC")

# test
# Client interface


client_request()
