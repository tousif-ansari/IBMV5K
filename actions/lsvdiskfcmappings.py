from lib.actions import BaseAction
class lsvdiskfcmappings(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdiskfcmappings -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s