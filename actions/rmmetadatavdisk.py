from lib.actions import BaseAction
class rmmetadatavdisk(BaseAction):
    def run(self,ip,username,password):
        command='rmmetadatavdisk -ignorevvolsexist '
        s = self.inputs(command,ip,username,password)
        return s