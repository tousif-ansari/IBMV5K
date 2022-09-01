from lib.actions import BaseAction
class recoverarray(BaseAction):
    def run(self, arrayName,members,ip,username,password):
        command='recoverarray "-' + arrayName + '":'+members+''
        s = self.inputs(command,ip,username,password)
        return s