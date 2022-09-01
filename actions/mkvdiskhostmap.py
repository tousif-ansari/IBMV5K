from lib.actions import BaseAction
class mkvdiskhostmap(BaseAction):
    def run(self,host,scsi,ip,username,password):
        command='mkvdiskhostmap -host '+str(host) +'-scsi '+str(scsi)
        s = self.inputs(command,ip,username,password)
        return s