from lib.actions import BaseAction
class lsvdiskanalysisprogress(BaseAction):
    def run(self,ip,username,password):
        command='lsvdiskanalysisprogress'
        s = self.inputs(command,ip,username,password)
        return s