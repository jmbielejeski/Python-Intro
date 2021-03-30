print('Hello, world!')

my_name = "John"

my_rate = 40

my_income = my_rate * 2080

print('my name is', my_name, 'and I make ', my_income, 'per year')

def say_hi(x):
  print('Hi', x)

say_hi(my_name)

def add_numbers(x, y):
  print(x + y)

add_numbers(21, 333)

door_is_locked = False

if door_is_locked:
  print('the door is locked')
else:
  print('the door is open')

for letter in 'Hello World':
  print(letter)

mylist = [1, 'a', 'Hello']
for item in mylist:
  print(item)

i = 1
while i < 6:
  print(i)
  i = i + 1

def say_hi(name):
  if name == '':
    print('you didnt enter your name')
  else:
    print('Hi There...')
    for letter in name:
      print(letter)
      
name = input()
say_hi(name)

dir(5)

class Car:
  speed = 0
  started = False

  def start(self):
    self.started = True
    print('Car has been started')

  def increase_speed(self, delta):
    if self.started:
      self.speed = self.speed + delta
      print('Vrooooom')
    else:
      print('You need to start the car first')

  def stop(self):
    self.speed = 0
    print('Stopping')

car = Car()
car.increase_speed(10)

car.start()

car.increase_speed(40)

car.stop()

fizz_or_buzz = ''
def fizz_buzz(number):
  if number % 15 == 0:
    fizz_or_buzz = 'FizzBuzz'
    print(fizz_or_buzz)
  elif number % 5 == 0:
    fizz_or_buzz = 'Fizz'
    print(fizz_or_buzz)
  else:
    fizz_or_buzz = 'Buzz'
    print(fizz_or_buzz)

fizz_buzz(15)
fizz_buzz(25)
fizz_buzz(27)