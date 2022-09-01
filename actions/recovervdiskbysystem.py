from lib.actions import BaseAction
class aliadd(BaseAction):
    def run(self,ip,username,password):
        command='recovervdiskbysystem'
        s = self.inputs(command,ip,username,password)
        return s