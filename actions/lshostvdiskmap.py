from lib.actions import BaseAction
class lshostvdiskmap(BaseAction):
    def run(self, delim,ip,username,password):
        command='lshostvdiskmap -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s