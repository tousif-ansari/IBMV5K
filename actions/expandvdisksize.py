from lib.actions import BaseAction
class expandvdisksize(BaseAction):
    def run(self, size,unit,mdisk,fmtdisk,ip,username,password):
        command='expandvdisksize -size ' + str(size) +'-unit ' + str(unit) + '-mdisk ' + str(mdisk) + '-fmtdisk ' + str(fmtdisk)
        s = self.inputs(command,ip,username,password)
        return s