from lib.actions import BaseAction
class lsrepairvdiskcopyprogress(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsrepairvdiskcopyprogress -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s