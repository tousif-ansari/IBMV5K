from lib.actions import BaseAction
class rmarray(BaseAction):
    def run(self, mdisk,ip,username,password):
        command='rmarray -mdisk ' +str(mdisk)
        s = self.inputs(command,ip,username,password)
        return s