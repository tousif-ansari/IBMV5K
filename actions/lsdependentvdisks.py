from lib.actions import BaseAction
class lsdependentvdisk(BaseAction):
    def run(self, delim,drive,ip,username,password):
        command='lsdependentvdisks -delim : '+str(delim)+'-drive ' +str(drive)
        s = self.inputs(command,ip,username,password)
        return s