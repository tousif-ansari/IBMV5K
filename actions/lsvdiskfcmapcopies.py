from lib.actions import BaseAction
class lsvdiskfcmapcopies(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdiskfcmapcopies -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s