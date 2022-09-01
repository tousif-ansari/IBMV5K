from lib.actions import BaseAction
class lsrepairsevdiskcopyprogress(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsrepairsevdiskcopyprogress -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s