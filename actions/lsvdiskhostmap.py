from lib.actions import BaseAction
class lsvdiskfcmappings(BaseAction):
    def run(self, map,ip,username,password):
        command='lsvdiskfcmappings '+str(map)
        s = self.inputs(command,ip,username,password)
        return s