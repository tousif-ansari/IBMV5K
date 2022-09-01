from lib.actions import BaseAction
class addvolumecopy(BaseAction):
    def run(self,poolName,ip,username,password):
        command='addvolumecopy -pool ' + str(poolName)
        s=self.inputs(command,ip,username,password)
        return s