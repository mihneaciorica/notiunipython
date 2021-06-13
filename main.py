"""

Details:

Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".

class Vehicle:
   def __init__(self, Make, Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
       self.Make=Make
       self.Model=Model
       self.Year=Year
       self.Weight=Weight
       self.NeedsMaintenance=NeedsMaintenance
       self.TripsSinceMaintenance=TripsSinceMaintenance

class Cars:
   def __init__(self, Make, Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0,isDriving):
       Vehicle.__init__(self, Make, Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0)
       self.isDriving=isDriving
   def Drive():
       self.isDriving=True
   def Stop():
       self.isDriving=False
       self.TripsSinceMaintenance+=1
       if self.TripsSinceMaintenance>100:
          self.NeedsMaintenance=True
   def Repair(self):
       self.TripsSinceMaintenance=0
       self.NeedsMaintenance=False






The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method called "Stop" that sets the value of isDriving to false.

Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), and an error message should be printed saying that the plane can't fly until it's repaired.

"""

class Vehicle:
   def __init__(self, Make, Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
       self.Make=Make
       self.Model=Model
       self.Year=Year
       self.Weight=Weight
       self.NeedsMaintenance=NeedsMaintenance
       self.TripsSinceMaintenance=TripsSinceMaintenance

class Car:
   def __init__(self, Make, Model,Year,Weight,isDriving,NeedsMaintenance=False,TripsSinceMaintenance=0):
       Vehicle.__init__(self, Make, Model,Year,Weight,NeedsMaintenance=False,TripsSinceMaintenance=0)
       self.isDriving=isDriving
   def Drive(self):
       self.isDriving=True
   def Stop(self):
       self.isDriving=False
       self.TripsSinceMaintenance+=1
       if self.TripsSinceMaintenance>100:
          self.NeedsMaintenance=True
   def Repair(self):
       self.TripsSinceMaintenance=0
       self.NeedsMaintenance=False
Car_one=Car('Renault','Safrane',1996,2000,False,TripsSinceMaintenance=0,)
Car_one.Drive()
if Car_one.isDriving==True:
    print('I took Car One for a drive')
Car_one.Stop()
print(Car_one.Make)
print(Car_one.Model)
print(Car_one.Year)
print(Car_one.Weight)
print(Car_one.NeedsMaintenance)
print(Car_one.TripsSinceMaintenance)

Car_two=Car('Renault','Clio',1996,1600,False,100)
print('this is an older one')
Car_two.TripsSinceMaintenance=100
Car_two.Drive()
if Car_two.isDriving==True:
    print('I took Car Two for a drive')
Car_two.Stop()
print(Car_two.Make)
print(Car_two.Model)
print(Car_two.Year)
print(Car_two.Weight)
print('an it needs maintenance')
print(Car_two.NeedsMaintenance)
print(Car_two.TripsSinceMaintenance)

Car_three=Car('Renault','Avantime',2000,2200,False,0)
Car_three.TripsSinceMaintenance=56
Car_three.Drive()
if Car_three.isDriving==True:
    print('I took Car Three for a drive')
Car_three.Stop()
Car_three.Drive()
if Car_three.isDriving==True:
    print('I took Car Three for a drive')
Car_three.Stop()
Car_three.Drive()
if Car_three.isDriving==True:
    print('I took Car Three for a drive')
Car_three.Stop()
Car_three.Drive()
if Car_three.isDriving==True:
    print('I took Car Three for a drive')
Car_three.Stop()
print(Car_three.Make)
print(Car_three.Model)
print(Car_three.Year)
print(Car_three.Weight)
print(Car_three.NeedsMaintenance)
print(Car_three.TripsSinceMaintenance)
Car_three.Repair()
print('Repairing car_three...so now resetting the trips counter to:')
print(Car_three.TripsSinceMaintenance)