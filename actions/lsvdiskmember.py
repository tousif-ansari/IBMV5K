from lib.actions import BaseAction
class lsvdiskmember(BaseAction):
    def run(self, member,ip,username,password):
        command='lsvdiskmember '+str(member)
        s = self.inputs(command,ip,username,password)
        return s