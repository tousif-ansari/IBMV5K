from lib.actions import BaseAction
class lsarraymember(BaseAction):
    def run(self,delimName,ip,username,password):
        command='lsarraymember -delim : " '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s