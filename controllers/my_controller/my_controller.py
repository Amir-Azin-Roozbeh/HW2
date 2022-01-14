from controller import Robot, Lidar, Camera
import csv

MAX_SPEED = 6.28


if __name__ == '__main__':
    
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    leftMotor = robot.getDevice('left wheel motor')
    rightMotor = robot.getDevice('right wheel motor')
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    
    leftMotor.setVelocity(0)
    rightMotor.setVelocity(0) 
    
    lidar = Lidar('lidar')
    lidar.enable(timestep)
    range_image = []
    
    camera = Camera('camera')
    camera.enable(timestep)
    
    
    counter = 0;
    
    while robot.step(timestep) != -1 and counter != 100:
        counter += 1
        camera.saveImage('imageCamera.png', 100)
        # range_image = lidar.getRangeImage()
        # print("{}".format(range_image))
        # print(len(range_image))
    
       
    # f = open('data.csv', 'w')
    # writer = csv.writer(f)        
    # writer.writerow(range_image)
    # f.close()
        
        # leftMotor.setVelocity(MAX_SPEED * 0)
        # rightMotor.setVelocity(MAX_SPEED * 0)
        