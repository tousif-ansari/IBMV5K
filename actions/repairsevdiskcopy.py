from lib.actions import BaseAction
class repairsevdiskcopy(BaseAction):
    def run(self, diskname,ip,username,password):
        command='repairsevdiskcopy '+str(diskname)
        s = self.inputs(command,ip,username,password)
        return s