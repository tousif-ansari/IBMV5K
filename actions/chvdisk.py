from lib.actions import BaseAction
class chvdisk(BaseAction):
    def run(self, rate,ip,username,password):
        command='chvdisk -rate ' + str(rate)
        s = self.inputs(command,ip,username,password)
        return s