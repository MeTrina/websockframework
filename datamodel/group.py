__author__ = 'amen'
from sqlalchemy import *
import dbconfig
class Group(dbconfig.DBBase):
    __tablename__ = 'group'
    gid=Column(BigInteger,autoincrement=True,primary_key=True,nullable=False)
    creator=Column(BigInteger,nullable=False,index=True)
    group_name=Column(String(256),nullable=False)
    group_board=Column(String(4096))
    type=Column(Integer)
    time=Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))
    __table_args__=({'mysql_engine':'MyISAM'},)
    def toJson(self):
        return {'gid':self.gid,
                "creator":self.creator,
                "name":self.group_name,
                "board":self.group_board,
                "type":self.type,
                "time":self.time}

class GroupWatchUpdate(dbconfig.DBBase):
    __tablename__ = 'group_watch'
    uid=Column(BigInteger,primary_key=True,nullable=False,autoincrement=False)
    gid=Column(BigInteger,nullable=False,index=True)
    __table_args__=({'mysql_engine':'MyISAM'},)