from lib.actions import BaseAction
class lsarraymemberprogress(BaseAction):
    def run(self, delimName,ip,username,password):
        command='lsarraymemberprogress -delim : " '+str(delimName)
        s = self.inputs(command,ip,username,password)
        return s