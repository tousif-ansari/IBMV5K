from lib.actions import BaseAction
class splitvdiskcopy(BaseAction):
    def run(self,copy,group,node,accessiogrp,ip,username,password):
        command='splitvdiskcopy -copy '+str(copy)+'-iogrp ' +str(group) +'-node ' +str(node)+'-accessiogrp' +str(accessiogrp)
        s = self.inputs(command,ip,username,password)
        return s