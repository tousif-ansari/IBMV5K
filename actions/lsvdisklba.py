from lib.actions import BaseAction
class lsvdisklba(BaseAction):
    def run(self, mdisk,mdisklba,ip,username,password):
        command='lsvdisklba -mdisk '+str(mdisk)+'mdisklbqa '+str(mdisklba)
        s = self.inputs(command,ip,username,password)
        return s