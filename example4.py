from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 5


# Jouw python instructies zet je vanaf hier:
for move in range(2):
    robotArm.grab()
    for right in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for left in range(2):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for move in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()









# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
