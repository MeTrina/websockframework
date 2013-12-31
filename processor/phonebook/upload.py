from datamodel.phone_book import PhoneBook
from tools.addPushQueue import AddPhoneBookUpdated
from tools.helper import Res
from tools.session import CheckSession

__author__ = 'amen'
import BackEndEnvData
import dbconfig
@CheckSession
def run(phone_list):
    session=dbconfig.Session()
    for one in phone_list:
        pb=PhoneBook()
        pb.uid=BackEndEnvData.uid
        pb.phone=one['phone']
        pb.name=one.get('name')
        session.merge(pb)
    session.commit()
    AddPhoneBookUpdated(BackEndEnvData.uid)
    return Res()