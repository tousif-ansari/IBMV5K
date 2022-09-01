from lib.actions import BaseAction
class rmvolumecopy(BaseAction):
    def run(self, site,ip,username,password):
        command='rmvolumecopy -site '+str(site)
        s = self.inputs(command,ip,username,password)
        return s