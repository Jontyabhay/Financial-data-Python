def ground_cost(weight):
  if (weight <= 2):
    return 1.5*weight+20
  elif (weight>2) and (weight<=6):
    return 3.00*weight+20
  elif (weight>6) and (weight<=10):
    return 4.00*weight+20
  elif (weight>10):
    return 4.75*weight+20

print(ground_cost(8.4))
premium_ground = 125

def drone_cost(weight):
  if (weight <= 2):
    return weight*4.5
  elif (weight>2) and (weight<=6):
    return weight*9.00
  elif (weight>6) and (weight<=10):
    return weight*12.00
  elif (weight>10):
    return weight*14.25

print(drone_cost(1.5))

def cheap_shipping(weight):
  if(ground_cost(weight) > drone_cost(weight)) and (ground_cost(weight)>premium_ground):
    return 'Drone shipping is cheapest with ' + str(drone_cost(weight))
  elif (ground_cost(weight) < drone_cost(weight)):
    return "Ground shipping is cheapest with " + str(ground_cost(weight))

print(cheap_shipping(4.8))


