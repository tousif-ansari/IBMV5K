from lib.actions import BaseAction
class lsvdiskaccess(BaseAction):
    def run(self, disk,ip,username,password):
        command='lsvdiskaccess '+str(disk)
        s = self.inputs(command,ip,username,password)
        return s