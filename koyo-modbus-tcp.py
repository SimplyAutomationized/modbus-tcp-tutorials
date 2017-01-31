from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from time import sleep

"""
Modbus address 317511 -- 317600, (417511 -- 417600)*
1 -- Version of Device
2 -- Family
3 -- Processor
4 -- Module Type
5 -- Status Code
(6--8) -- Ethernet Address
9 -- RAM Size
10 -- Flash Size
11 -- Batt RAM Size
12 -- DIP Settings
13 -- Media Type
(14--15) -- EPF Count (if supported)
16 -- Run Relay State (if supported)
17 -- Batt Low (if supported)
18 -- Model Number
19 -- Ethernet Speed
(20--90) -- Reserved

Modbus Address 317501 -- 317506, (417501 -- 417506)*
1 -- OS Major Version
2 -- OS Minor Version
3 -- OS Build Version
4 -- Booter Major Version
5 -- Booter Minor Version
6 -- Booter Build Version
should be
Booter Version:	4.0.165
OS Version:	4.0.334

"""


class Koyo:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self._koyo = ModbusClient(ip_address)
        print self._koyo.connect()
        if self._koyo.connect():
            self._getversions()
            self._get_device_info()

    def _getversions(self):
        data = self._koyo.read_input_registers(17500, 6)
        self.os_version = '.'.join(map(str, data.registers[0:3]))
        self.boot_version = '.'.join(map(str, data.registers[3:6]))

    def _get_device_info(self):
        data = self._koyo.read_input_registers(17510, 19)
        self.device_version = data.registers[0]
        self.family = data.registers[1]

    def outputs(self, max=16):
        pass

    def write_output(self, output, value):
        pass

    def inputs(self, max=24):
        pass

    def memory_bits(self, bit):
        pass

    def disconnect(self):
        self._koyo.close()


if __name__ == '__main__':
    dl_06 = Koyo('10.10.55.99')  # ip address goes here
    print dl_06.os_version, dl_06.boot_version
    dl_06.disconnect()
