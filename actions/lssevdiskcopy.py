from lib.actions import BaseAction
class lssevdiskcopy(BaseAction):
    def run(self, delim,ip,username,password):
        command='lssevdiskcopy -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s