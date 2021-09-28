# forever-young
## F1.4.01.L1
### 1.
```python
getal = int(input("Tafel van "))
for number in range (1,11):
    print(str(number) + " x "+ str(getal) + " = " + str(number*getal))
```
### 2.
``` python
for aftel in range(30,-1,-1):
    print("rocket launching in: " + str(aftel))
print("")
print("Ready for takeoff")
print("                 ")
print("        /\       ")
print("       /  \      ")
print("      /    \     ")
print("      |    |     ")
print("      |    |     ")
print("      |    |     ")
print("      |    |     ")
print("      |    |     ")
print("     /      \    ")
print("     --    --    ")
print("     vvvvvvvv    ")
```
### 3.
```python
for time in range(1,13):
    print(str(time) + ":00 am")

for time in range(1,13):
    print(str(time) + ":00 pm")
```
### 4.
```python
for number in range(20,52,2):
    print(number)
```
## F1.4.01.O2
### Oefening 1
```python
robotArm.moveRight();
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
```
### Oefening 2
```python
robotArm.grab()
for right in range(9):
    robotArm.moveRight()
robotArm.drop()
for left in range(5):
    robotArm.moveLeft()
robotArm.grab()
for right in range(5):
    robotArm.moveRight()
robotArm.drop()
for left in range(2):
    robotArm.moveLeft()
robotArm.grab()
for right in range(5):
    robotArm.moveRight()
robotArm.drop()
```
### Oefening 3
```python
for move in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
```
### Oefening 4
```python
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
```
### Oefening 6
```python
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
```
