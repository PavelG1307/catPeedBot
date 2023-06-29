
from datetime import datetime

class User:
    id: int
    lastKaka: datetime = None
    lastPipi: datetime = None

    def __init__(self, id):
        self.id = id

    def updatePipi(self):
        self.lastPipi = datetime.now()

    def updateKaka(self):
        self.lastKaka = datetime.now()

