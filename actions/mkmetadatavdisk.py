from lib.actions import BaseAction
class mkmetadatavdisk(BaseAction):
    def run(self, group,ip,username,password):
        command='mkmetadatavdisk -mdiskgrp '+str(group)
        s = self.inputs(command,ip,username,password)
        return s