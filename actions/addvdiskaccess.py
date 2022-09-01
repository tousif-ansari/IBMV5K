from lib.actions import BaseAction
class addvdiskaccess(BaseAction):
    def run(self,iogrp,ip,username,password):
        command='addvdiskaccess -iogrp '+str(iogrp)
        s=self.inputs(command,ip,username,password)
        return s


