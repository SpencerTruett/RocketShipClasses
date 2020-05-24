from Rocket import Rocket

# Create a Rocket object.
#myRocket = Rocket()
#print("Rocket altitude:", myRocket.y)

#myRocket.move_up()
#print("Rocket altitude:", myRocket.y)

#myRocket.move_up()
#print("Rocket altitude:", myRocket.y)

# Create a fleet of 5 rockets, and store them in a list.
rocketFleet = []
for x in range(0,5):
    newRocket = Rocket()
    rocketFleet.append(newRocket)

rocketFleet[0].move_up()
rocketFleet[0].move_up()
rocketFleet[0].move_up()
rocketFleet[2].move_up()
rocketFleet[1].move_up()
rocketFleet[4].move_up()
rocketFleet[4].move_up()
rocketFleet[3].move_up()


rocketFleet[0].move_up()# Show that each rocket is a separate object.
for rocket in rocketFleet:
    print("Rocket altitude:", rocket.y)
