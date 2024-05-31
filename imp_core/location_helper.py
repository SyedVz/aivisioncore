import sys, time, threading, abc, signal
from threading import Event
from collections import deque


class Location_Helper(threading.Thread):

    def __init__(self, stop_event, real_data=False, route_file=None, google_route=False):
        super().__init__(group=None, name='car_location_helper')
        self.evt = stop_event
        
        self.real_data = real_data

        self.msgCnt = 0
        self.lat = 407344084
        self.long = -745384722
        self.elev = 139
        speed_in_mph = 96
        speed_in_kph = speed_in_mph * 1.61          # in km per hour
        speed_in_mps = speed_in_kph * 1000 / 3600   # in meter per sec
        self.speed_bsm = int(speed_in_mps * 50.0)        # Integer Units of 0.02 m/s
        self.heading = 1

        # Load BSM data from file
        self.saved_car_route = None
        self.saved_car_route_len = 0

        if (route_file == None):
            self.telemetry_file = "imp_core/vz_data/telemetry_input_arizona.csv"
        else:
            self.telemetry_file = route_file

        self.google_route = google_route

        with open (self.telemetry_file) as f:
            self.saved_car_route = f.readlines()
            # For google route I dont add a header line. For saved route remove the header
            if (not self.google_route):
                del self.saved_car_route[0]    # Delete the row with col titles
            self.saved_car_route_len = len(self.saved_car_route)

    def run(self):
        
        print("Starting Location Helper thread")

        # Start a thread to process incoming messages from GenAI
        threading.Thread(target=self.update_location).start()
        
        self.evt.wait()        
        self.vzmode_mqtt_client.disconnect()
        print("Ending Location Helper")

    def update_location(self):
        if (self.real_data):
            # get from GPS / RTK
            pass
        else:
            while (True):
                if (self.google_route):
                    self.update_saved_location_from_google_klm()
                else:
                    self.update_saved_location_data()

    def update_saved_location_data(self):
        prev_wait_time = 0
        gps_wait_time = 0
        wait_time = 0

        for i in range(0, self.saved_car_route_len):
            line = self.saved_car_route[i]
            cols = line.split(",")
            self.msgCnt = i % 128 #int(cols[1])
            self.lat = int(float(cols[3]) * 10000000)        # Convert to Int J2735 format
            self.long = int(float(cols[4]) * 10000000)       # Convert to Int J2735 format
            self.elev = float(cols[5])
            speed_in_mph = float(cols[9])
            speed_in_kph = speed_in_mph * 1.61          # in km per hour
            speed_in_mps = speed_in_kph * 1000 / 3600   # in meter per sec
            self.speed_bsm = int(speed_in_mps * 50.0)        # Integer Units of 0.02 m/s
            self.heading = float(cols[10])

            gps_wait_time = int(cols[2])

            if (prev_wait_time > 0):
                wait_time = gps_wait_time - prev_wait_time

            if (wait_time < 0):
                wait_time = wait_time + 60000 # Its less becasue gps seconds is in next second. So add a second

            # At the end update prev_wait_time
            prev_wait_time = gps_wait_time
            time.sleep(wait_time/1000)

    def update_saved_location_from_google_klm(self):

        wait_time = 0

        for i in range(0, self.saved_car_route_len):
            line = self.saved_car_route[i]
            cols = line.split(",")
            self.msgCnt = i % 128
            self.lat = int(float(cols[1]) * 10000000)        # Convert to Int J2735 format
            self.long = int(float(cols[0]) * 10000000)       # Convert to Int J2735 format
            self.elev = float(139)
            speed_in_mph = float(35)
            speed_in_kph = speed_in_mph * 1.61          # in km per hour
            speed_in_mps = speed_in_kph * 1000 / 3600   # in meter per sec
            self.speed_bsm = int(speed_in_mps * 50.0)        # Integer Units of 0.02 m/s
            self.heading = float(350)

            time.sleep(1)

    
