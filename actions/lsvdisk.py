from lib.actions import BaseAction
class lsvdisk(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsvdisk -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s