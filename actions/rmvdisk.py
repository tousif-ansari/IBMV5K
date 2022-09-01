from lib.actions import BaseAction
class rmvdisk(BaseAction):
    def run(self, diskname,ip,username,password):
        command='rmvdisk -force '+str(diskname)
        s = self.inputs(command,ip,username,password)
        return s