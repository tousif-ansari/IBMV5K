from lib.actions import BaseAction
class lsarrayinitprogress(BaseAction):
    def run(self, delimName,ip,username,password):
        command='lsarrayinitprogress -delim : '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s