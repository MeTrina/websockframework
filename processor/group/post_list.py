from sqlalchemy import and_
from datamodel.post import Post
from datamodel.post_like import PostLike
from tools.helper import Res, GetFileLink
from tools.session import CheckSession

__author__ = 'amen'
import BackEndEnvData
import dbconfig
def PostToJson(post):
    data= {'postid':post.postid,
            'uid':post.uid,
            'content':post.content,
            'like':post.like,
            'replycount':post.replycount,
            'time':post.time
            }
    if post.picture:
        data['picture']=GetFileLink(post.picture)
        data['width']=post.width
        data['height']=post.height
    if post.video:
        data['video']=GetFileLink(post.video)
        data['lenght']=post.lenght
    if post.voice:
        data['voice']=GetFileLink(post.voice)
        data['lenght']=post.lenght
    return data

@CheckSession
def run(gid,pos=0,count=50):
    session=dbconfig.Session()
    query=session.query(Post).filter(Post.group_id==gid).order_by(Post.postid.desc())
    if pos>0:
        query=query.offset(pos)
    query=query.limit(count)
    posts=query.all()
    plist=[]
    for post in posts:
        pdata=PostToJson(post)
        ilike_record=session.query(PostLike).filter(and_(PostLike.postid==post.postid,PostLike.uid==BackEndEnvData.uid)).first()
        pdata['ilike']=True if ilike_record is not None else False
        plist.append(pdata)
    session.close()
    return Res({'posts':plist})