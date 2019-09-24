from sympy import Matrix

# INITIAL CONDITIONS
# position [m]
x0 = 0
y0 = 0
z0 = 30
# velocity [m/s]
xd0 = 0
yd0 = 0
zd0 = 0
# orientation [rad]
thYaw0 = 0
thPitch0 = 0
thRoll0 = 0
# angular rates [rad/s]
thYawd0 = 0
thPitchd0 = 0
thRolld0 = 0

initConditions = Matrix([x0, y0, z0, xd0, yd0, zd0, thYaw0, thPitch0, thRoll0, thYawd0, thPitchd0, thRolld0])