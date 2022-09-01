from lib.actions import BaseAction
class rmvolumne(BaseAction):
    def run(self, volume,ip,username,password):
        command='rmvolume '+str(volume)
        s = self.inputs(command,ip,username,password)
        return s