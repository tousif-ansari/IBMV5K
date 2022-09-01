from lib.actions import BaseAction
class analyzevdiskbysystem(BaseAction):
    def run(self,ip,username,password):
        command='analyzevdiskbysystem'
        s = self.inputs(command,ip,username,password)
        return s