import time
import socket
import simulator

IP_ADDRESS = "127.0.0.1"
PORT = 45000
# we create the class intermediateDevice
class IntermediateDevice():
   """
   Intermediate device class
   """
   def __init__(self, ip, port):
       """
        Create client socket
       """
       
       self.sensorSim = simulator.SensorSimulator()
       self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.socket.connect((ip, port))
       # We start the start of time, from our counter in this way we mark the beginning
       self.sensor_data = ""
       self.time0 = time.time()
       """
       Client main task:
       Create random data of the sensors every 0.5 seconds. After 5 seconds,
       the intermediate device will send all the generated data to the final
       device
       """
       '''
       In this way, what we intend to achieve is that it distinguishes when the 
       list is empty and when it is not,
       since when the sleep time passes, it will be contained in 'sensors', 
       therefore we will have to concatenate it.
       
       '''

   def run(self):
       
       while True:
          self.sensorSim.simulate()
          if self.sensor_data == "":
             self.sensor_data = str(self.sensorSim.sensors)
          else:
             self.sensor_data = self.sensor_data + ',' + str(self.sensorSim.sensors)

          # print(self.sensor_data)
          '''
          We do the calculation to make the shipment in the required time
          time0 = time.time()
          time.sleep(0.5)
          dt = time.time() - time0
          w=time.time()
          print(time0)
          print(w)
          print(dt)
            1681230169.6622658
            1681230170.1623843
            0.5001144409179688
          '''
          time.sleep(0.5)
          dt = time.time() - self.time0
          

          # Send data to the final device every 0.5 seconds
          # We update the start counter, in the current time (after 0.5s)
          if dt > 5:
             self.sendData(self.sensor_data)
             self.sensor_data = ""
             self.time0 = time.time()
             
      

   def sendData(self, data):
       """
       Send data to the server socket
       """
       print("sending data to the server...")
       self.socket.send(data.encode('utf8'))


if __name__ == '__main__':
   client = IntermediateDevice(IP_ADDRESS, PORT)
   client.run()
