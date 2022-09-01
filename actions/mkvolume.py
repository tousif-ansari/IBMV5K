from lib.actions import BaseAction
class mkvolume(BaseAction):
    def run(self, pool,size,ip,username,password):
        command='mkvolume -pool '+str(pool) +'-size '+str(size)
        s = self.inputs(command,ip,username,password)
        return s