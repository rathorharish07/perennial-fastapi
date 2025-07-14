from enum import Enum

class Department(Enum): 
    hr="hr"
    it="it"
    finance="finance"


class Location(Enum):
    dh="ny"
    mh="sf"
    ind="la"

class Status(Enum):
    active="active"
    inactive="inactive"
    suspended="suspended"


