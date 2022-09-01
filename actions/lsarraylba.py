from lib.actions import BaseAction
class lsarraylba(BaseAction):
    def run(self, delimName,ip,username,password):
        command='lsarraylba -delim : " '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s