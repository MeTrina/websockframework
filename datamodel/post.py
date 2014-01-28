#coding:utf-8
__author__ = 'amen'
from sqlalchemy import *
import dbconfig
import time
class Post(dbconfig.DBBase):
    __tablename__ = 'post'
    postid=Column(BigInteger,autoincrement=True,primary_key=True,nullable=False)
    uid=Column(BigInteger,nullable=False,index=True)
    group_id=Column(BigInteger,default=0)
    content=Column(String(4096))
    picture=Column(String(1024))
    video=Column(String(1024))
    voice=Column(String(1024))
    width=Column(Integer)
    height=Column(Integer)
    length=Column(Integer)
    like=Column(Integer,default=0)
    replycount=Column(Integer,default=0)
    time=Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))
    def toJson(post):
        data= {'postid':post.postid,
                'uid':post.uid,
                'gid':post.group_id,
                'like':post.like,
                'replycount':post.replycount,
                'time':post.time
                }
        if post.content:
            data['type']='txt'
            data['content']=post.content
        elif post.picture:
            data['type']='pic'
            data['picture']=post.picture
            data['width']=post.width
            data['height']=post.height
        elif post.video:
            data['type']='vdo'
            data['video']=post.video
            data['length']=post.length
        elif post.voice:
            data['type']="vic"
            data['voice']=post.voice
            data['length']=post.length
        return data