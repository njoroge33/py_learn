# Two classes have been declared:
      class Car(object):
      def m1(self):
      print('car 1')
      def m2(self):
      print('car 2')
      def __str__(self):
      return "vroom"

      class Truck (Car):
      def m1(self):
      print('truck 1')
      def m2(self):
      super(Truck, self) 
# m1()
      def __str__(self):
      return super(Truck, self) 
# __str__() + super(Truck, self) 
# __str__() 
