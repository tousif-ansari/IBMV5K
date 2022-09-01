from lib.actions import BaseAction
class rmvdiskaccess(BaseAction):
    def run(self, groupname,ip,username,password):
        command='rmvdiskaccess -iogrp '+str(groupname)
        s = self.inputs(command,ip,username,password)
        return s