from lib.actions import BaseAction
class charraymember(BaseAction):
    def run(self, memberName,ip,username,password):
        command='charraymember -member' +str(memberName)
        s = self.inputs(command,ip,username,password)
        return s