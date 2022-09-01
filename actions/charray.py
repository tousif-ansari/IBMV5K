from lib.actions import BaseAction
class charray(BaseAction):
    def run(self, arrayName,ip,username,password):
        command='charray -name ' +str(arrayName)
        s = self.inputs(command,ip,username,password)
        return s