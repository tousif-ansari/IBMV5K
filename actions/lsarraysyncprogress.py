from lib.actions import BaseAction
class lsarraysyncprogress(BaseAction):
    def run(self, delimName,ip,username,password):
        command='lsarraysyncprogress -delim : " '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s