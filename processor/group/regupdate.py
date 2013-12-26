from datamodel.group import GroupWatchUpdate
from tools.helper import Res
from tools.session import CheckSession

__author__ = 'amen'
import BackEndEnvData
import dbconfig
@CheckSession
def run(gid):
    session=dbconfig.Session()
    watchg=GroupWatchUpdate()
    watchg.uid=BackEndEnvData.uid
    watchg.gid=gid
    session.merge(watchg)
    session.commit()
    return Res()