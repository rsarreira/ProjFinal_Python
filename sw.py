from datetime import datetime
from tickets import Tickets

class SW(Tickets):
    def __init__(self, *args):
        super().__init__()
        self.software = None
        self.necessidade = None

        if len(args) == 1 and isinstance(args[0] , SW):
            super().__init__(args[0])
            self.software = args[0].software
            self.necessidade = args[0].necessidade
        
        elif len(args) == 4:
            super().__init__(args[0] , args[1])            
            self.software = args[2]
            self.necessidade = args[3]

