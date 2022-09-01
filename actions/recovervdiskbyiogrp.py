from lib.actions import BaseAction
class recovervdiskbyiogrp(BaseAction):
    def run(self,groupname,ip,username,password):
        command='recovervdiskbyiogrp '+str(groupname)
        s = self.inputs(command,ip,username,password)
        return s