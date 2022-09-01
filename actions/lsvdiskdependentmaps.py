from lib.actions import BaseAction
class lsvdiskdependentmaps(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdiskdependentmaps -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s