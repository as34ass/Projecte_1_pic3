import time
import socket
import json
import datetime

IP_ADDRESS = "127.0.0.1"
PORT = 45000


class FinalDevice():
   """
   Class to implement the final device
   """
   def __init__(self, ip, port):

       "We make the connection to the server and wait for your response. "
       self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.socket.bind((ip, port))
       self.socket.listen()
       
       self.conn, _=self.socket.accept()
       print("client connected!")


   def savejsonfile(self, data):
      """
      Save received data from the intermediate device into a json file
      """
      # Json filename, create a header a title to the json file
      '''
      aa = datetime.datetime.now().strftime("%Y-%m-%dT_%H-%M-%S")+'.json'
      print (a)
      2023-04-11T_17-57-03.json
      '''
      json_filename = datetime.datetime.now().strftime("%Y-%m-%d_Hour_%H-%M-%S")+'.json'

      '''slipt the data recived document to separate 
       and dump the data into a json file 
       with the 'whit open' method and the name of the file that we want to be added
       qa=('prueva split, telecom prog')
         qa1=qa.split(',')
         print(qa1)

         with open(a, 'w') as outfile:
         for elem in qa:
            print(elem)
            json.dump(elem, outfile)
            outfile.write('\n')
            
         print (outfile)
         ['prueva split', ' telecom prog']
      '''
      data_split = data.split(',')
      with open(json_filename, 'w') as outfile:
         for elem in data_split:
            print(elem)
            json.dump(elem, outfile)
            outfile.write('\n')


      """
      Receive data from TCP socket n bit format with the utf8 
      format we can transform the most common characters without 
      having error problems in any character


         qa=('prueva split, telecom prog')
         qa1=qa.split(',')
         print(qa1)

         qa2=qa.encode('utf8')
         print(qa2)

         qa2=qa2.decode('utf8')
         print(qa2)S

         ['prueva split', ' telecom prog']
         b'prueva split, telecom prog'
         prueva split, telecom prog
      """
   def run(self):
      while True:
         text_decoded=self.conn.recv(6000).decode("utf8")
         self.savejsonfile(text_decoded)
          


if __name__ == '__main__':
   server = FinalDevice(IP_ADDRESS, PORT)
   server.run()
