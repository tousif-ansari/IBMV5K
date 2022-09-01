from lib.actions import BaseAction
class addvdiskcopy(BaseAction):
    def run(self, mdiskgrp,eazytier,ip,username,password):
        command='addvdiskcopy -mdiskgrp ' + str(mdiskgrp) + ' -eazytier ' + str(eazytier)
        s=self.inputs(command,ip,username,password)
        return s



