from lib.actions import BaseAction
class recoverarraybysystem(BaseAction):
    def run(self,ip,username,password):
        command='recoverarraybysystem'
        s = self.inputs(command,ip,username,password)
        return s