from lib.actions import BaseAction
class mkvdisk(BaseAction):
    def run(self, group,size,iogrp,vtype,mdisk,node,ip,username,password):
        command='mkvdisk -mdiskgrp '+str(group)+'-size ' +str(size) +'-iogrp ' +str(iogrp)+'-vtype' +str(vtype) +'-mdisk ' +str(mdisk) +'-node '+str(node)
        s = self.inputs(command,ip,username,password)
        return s