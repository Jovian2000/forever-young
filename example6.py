from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for right in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
