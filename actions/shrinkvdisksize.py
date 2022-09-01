from lib.actions import BaseAction
class shrinkvdisksize(BaseAction):
    def run(self, size,unit,ip,username,password):
        command='shrinkvdisksize -size '+str(size) + '-unit '+str(unit)
        s = self.inputs(command,ip,username,password)
        return s