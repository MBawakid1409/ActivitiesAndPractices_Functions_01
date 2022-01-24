# Activities & Practices

# 01 Which variables can be called in the blank spot in this code:
counter = 0
 
def update():
  new_counter = counter + 1
  return new_counter

# Answer: counter
# counter is global in scope, whereas new_counter only exists inside of update.

# 02 What line of code can be used to return a variable inner_var from a function back to the piece of code that called the function?

# Answer: return inner_var

# 03 What happens when you call report()?
time = "3pm"
mood = "good"
 
def report():
  print("The current time is " + time)
  print("The mood is " + mood)
 
print("Beginning of report")
 
report()

# Answer: Two strings are printed: "The current time is 3pm" and "The mood is good"

# 04 Given the following function, what will produce the output "There is no greater agony than bearing an untold story inside you."?
def quote(x):
  print("There is no greater agony than bearing " + x + " inside you.")

# Answer: quote("un untold story")
# Output: There is no greater agony than bearing un untold story inside you.  

# 05 How do you call update with a new_value of 20?
def update(new_value = 10):
  old_value = new_value
  return old_value

# Answer: update(20)  

# 06 What line of code will call force with a value of 10 for mass and a value of 9.81 for acceleration?
def force(mass, acceleration):
  force_val = mass*acceleration
  return force_val

# Answer: force(10, 9.81)  

# 07 How do you call a function called setup with no arguments?

# Answer: setup()

# Activity "Getting Ready for Physics Class"
# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
print("Turn up the Temperature")
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)  

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)  

print("----------------------------------")

print("Use the Force")

def get_force(mass, acceleration):
  result = mass * acceleration
  return result

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies {} Newtons of force.".format(train_force))

def get_energy(mass):
  c = 3*10**8
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies {} Joules.".format(bomb_energy))

print("----------------------------------")

print("Do the Work")


def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))
