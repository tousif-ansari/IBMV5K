from lib.actions import BaseAction
class movevdisk(BaseAction):
    def run(self, group,ip,username,password):
        command='movevdisk -iogrp '+str(group)
        s = self.inputs(command,ip,username,password)
        return s