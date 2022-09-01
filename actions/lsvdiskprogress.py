from lib.actions import BaseAction
class lsvdiskprogress(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdiskprogress -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s