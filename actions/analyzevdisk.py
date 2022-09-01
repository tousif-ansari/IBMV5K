from lib.actions import BaseAction
class analyzevdisk(BaseAction):
    def run(self, disk,ip,username,password):
        command='analyzevdisk ' + str(disk)
        s=self.inputs(command,ip,username,password)
        return s