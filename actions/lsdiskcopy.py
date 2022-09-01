from lib.actions import BaseAction
class lsdiskcopy(BaseAction):
    def run(self, delim,ip,username,password):
        command='lsdiskcopy -delim : '+str(delim)
        s = self.inputs(command,ip,username,password)
        return s