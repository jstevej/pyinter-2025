import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.resetSimulation()
p.setGravity(gravX=0, gravY=0, gravZ=-9.81)
p.setAdditionalSearchPath(path=pybullet_data.getDataPath())
# p.loadURDF(fileName='./cube.urdf', basePosition=[0, 0, 1])
plane = p.loadURDF("plane.urdf")
robot = p.loadURDF("r2d2.urdf", basePosition=[0, 0, 1])

joint_dict_info = {
    0: "joint Index",  #starts at 0
    1: "joint Name",
    2: "joint Type",  #0=revolute (rotational), 1=prismatic (sliding), 4=fixed
    3: "state vectorIndex",
    4: "velocity vectorIndex",
    5: "flags",  #nvm always 0
    6: "joint Damping",  
    7: "joint Friction",  #coefficient
    8: "joint lowerLimit",  #min angle
    9: "joint upperLimit",  #max angle
    10: "joint maxForce",  #max force allowed
    11: "joint maxVelocity",  #max speed
    12: "link Name",  #child link connected to this joint
    13: "joint Axis",
    14: "parent FramePos",  #position
    15: "parent FrameOrn",  #orientation
    16: "parent Index"  #−1 = base
}

for i in range(p.getNumJoints(bodyUniqueId=robot)):
    print(f"--- Joint {i} ---")
    joint_info = p.getJointInfo(bodyUniqueId=robot, jointIndex=i)
    for k in joint_dict_info.keys():
        print(f"{joint_dict_info[k]}: {joint_info[k]}")
    link_name = p.getJointInfo(robot, i)[12].decode("utf-8")
    dyn = p.getDynamicsInfo(robot, i)
    pos, orn, *_ = p.getLinkState(robot, i)
    link_info = { "Mass": dyn[0], "Friction": dyn[1], "Position": pos, "Orientation": orn }
    print(f"Link Info: {link_info}")


# settle down

for _ in range(240):
    p.stepSimulation()

right_wheels = [2, 3]
left_wheels = [6, 7]

# turn

print("Turning...")

for _ in range(240):
    for j in right_wheels:
        p.setJointMotorControl2(
            bodyUniqueId=robot,
            jointIndex=j,
            controlMode=p.VELOCITY_CONTROL,
            targetVelocity=-100,
            force=50.0
        )
    for j in left_wheels:
        p.setJointMotorControl2(
            bodyUniqueId=robot,
            jointIndex=j,
            controlMode=p.VELOCITY_CONTROL,
            targetVelocity=100,
            force=50.0
        )
    p.stepSimulation()
    time.sleep(1/240)

# move forward

print("Moving forward...")

all_wheels = right_wheels + left_wheels

for _ in range(500):
    for j in all_wheels:
        p.setJointMotorControl2(
            bodyUniqueId=robot,
            jointIndex=j,
            controlMode=p.VELOCITY_CONTROL,
            targetVelocity=-100,
            force=10.0
        )
        p.stepSimulation()
        time.sleep(1/240)

p.disconnect()
