from lib.actions import BaseAction
class lsvdiskanalysis(BaseAction):
    def run(self,ip,username,password):
        command='lsvdiskanalysis'
        s = self.inputs(command,ip,username,password)
        return s