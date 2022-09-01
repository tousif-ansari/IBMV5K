from lib.actions import BaseAction
class lsvdisksyncprogress(BaseAction):
    def run(self,ip,username,password):
        command='lsvdisksyncprogress'
        s = self.inputs(command,ip,username,password)
        return s