from lib.actions import BaseAction
class mkarray(BaseAction):
    def run(self, members,drive,ip,username,password):
        command='mkarray -level: '+str(members)+' -drive '+str(drive)
        s = self.inputs(command,ip,username,password)
        return s