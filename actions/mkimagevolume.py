from lib.actions import BaseAction
class mkimagevolume(BaseAction):
    def run(self, mdisk,pool,ip,username,password):
        command='mkimagevolume -mdisk '+str(mdisk) +'-pool '+str(pool)
        s = self.inputs(command,ip,username,password)
        return s