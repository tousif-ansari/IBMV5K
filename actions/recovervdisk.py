from lib.actions import BaseAction
class recovervdisk(BaseAction):
    def run(self, diskname,ip,username,password):
        command='recovervdisk '+str(diskname)
        s = self.inputs(command,ip,username,password)
        return s