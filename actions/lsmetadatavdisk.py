from lib.actions import BaseAction
class lsmetadatavdisk(BaseAction):
    def run(self,ip,username,password):
        command='lsmetadatavdisk'
        s = self.inputs(command,ip,username,password)
        return s