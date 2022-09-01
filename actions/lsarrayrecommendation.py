from lib.actions import BaseAction
class lsarrayrecommendation(BaseAction):
    def run(self, className,ip,username,password):
        command='lsarrayrecommendation -driveclass ' +str(className)
        s = self.inputs(command,ip,username,password)
        return s