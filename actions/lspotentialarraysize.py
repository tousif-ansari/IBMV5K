from lib.actions import BaseAction
class lspotentialarraysize(BaseAction):
    def run(self, driveClass,driveCount,level,stripWidth,rebuildareas,ip,username,password):
        command='lspotentialarraysize -driveclass ' +str(driveClass)+'-drivecount ' +str(driveCount) +'-level ' +str(level)+'-stripwidth' +str(stripWidth) +'-rebuildareas ' +str(rebuildareas)
        s = self.inputs(command,ip,username,password)
        return s