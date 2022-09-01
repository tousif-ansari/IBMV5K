from lib.actions import BaseAction
class lsarraymembergoal(BaseAction):
    def run(self,delimName,ip,username,password):
        command='lsarraymembergoal -delim : " '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s