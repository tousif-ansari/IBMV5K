from lib.actions import BaseAction
class lsarray(BaseAction):
    def run(self, delimName,ip,username,password):
        command='lsarray "-delim : "'+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s