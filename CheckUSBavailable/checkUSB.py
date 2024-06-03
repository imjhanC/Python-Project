import serial.tools.list_ports

def find_usb_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

print("Available ports:")
print(find_usb_ports())
