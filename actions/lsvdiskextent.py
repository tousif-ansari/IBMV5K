from lib.actions import BaseAction
class lsvdiskextent(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdiskextent -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s