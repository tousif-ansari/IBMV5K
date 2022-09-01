from lib.actions import BaseAction
class rmvdiskhostmap(BaseAction):
    def run(self, hostname,ip,username,password):
        command='rmvdiskhostmap -host '+str(hostname)
        s = self.inputs(command,ip,username,password)
        return s