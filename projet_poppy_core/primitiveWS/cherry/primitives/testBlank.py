import pypot.primitive

class TestBlank(pypot.primitive.Primitive):
    def run(self):
        poppy = self.robot

        for m in poppy.arms :
            m.compliant = False
        
        poppy.r_shoulder_y.goto_position(-50, 1, wait=False)
        poppy.r_shoulder_x.goto_position(-25, 1, wait=False)
        poppy.r_arm_z.goto_position(-35, 1, wait=False)
        poppy.r_elbow_y.goto_position(10, 1, wait=False)

        poppy.l_shoulder_y.goto_position(-5, 1, wait=False)
        poppy.l_shoulder_x.goto_position(5, 1, wait=False)
        poppy.l_arm_z.goto_position(-45, 1, wait=False)
        poppy.l_elbow_y.goto_position(-15, 1, wait=True)
