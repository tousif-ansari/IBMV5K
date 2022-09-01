from lib.actions import BaseAction
class rmvdiskcopy(BaseAction):
    def run(self, name,ip,username,password):
        command='rmvdiskcopy -copy '+str(name)
        s = self.inputs(command,ip,username,password)
        return s