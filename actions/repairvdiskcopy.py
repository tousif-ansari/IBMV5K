from lib.actions import BaseAction
class repairsevdiskcopy(BaseAction):
    def run(self, startlba,ip,username,password):
        command='repairsevdiskcopy -resync ''-startlba'+str(startlba)
        s = self.inputs(command,ip,username,password)
        return s