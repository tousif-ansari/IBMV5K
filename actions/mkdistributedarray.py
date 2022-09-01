from lib.actions import BaseAction
class mkdistributedarray(BaseAction):
    def run(self, level,driveclass,drivecount,stripwidth,rebuildareas,ip,username,password):
        command='mkdistributedarray --level ' +str(-level)+'-driveclass ' +str(driveclass) +'-drivecount ' +str(drivecount)+'-stripewidth' +str(stripwidth) +'-rebuildareas ' +str(rebuildareas)
        s = self.inputs(command,ip,username,password)
        return s