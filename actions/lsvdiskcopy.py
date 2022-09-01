from lib.actions import BaseAction
class lsvdiskcopy(BaseAction):
    def run(self,delim,ip,username,password):
        command='lsvdisk -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s