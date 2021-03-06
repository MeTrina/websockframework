#coding:utf-8
__author__ = 'amen'
import json

import qiniu.rs
import web

import WebSiteBasePage
import dbconfig
import datamodel.user
import website_config


class HeadImg(WebSiteBasePage.AutoPage):
    def GET(self):
        params=web.input(usepage='0')
        sessionid=params.get('sessionid',None)
        if sessionid is None:
            return "No Session id"
        data=dbconfig.redisdb.get(str('session:%s'%sessionid))
        if data is None:
            return {"errno":1,"error":"session not found","result":{}}
        data=json.loads(data)
        policy = qiniu.rs.PutPolicy(dbconfig.qiniuSpace)
        policy.callbackUrl='http://%s/upload/HeadImgDone'%website_config.hostname
        policy.callbackBody='{"name":"$(fname)","hash":"$(etag)","width":$(imageInfo.width),"height":$(imageInfo.height),' +\
                            '"uid":%d}'%data['uid']
        uptoken = policy.token()
        if int(params['usepage'])==0:
            web.header("Content-type","application/json")
            return json.dumps({'token':uptoken})
        tpl=WebSiteBasePage.jinja2_env.get_template('upload/HeadImg.html')
        return tpl.render(token=uptoken)
    def POST(self):
        pass

class HeadImgDone(WebSiteBasePage.AutoPage):
    SITE="http://%s.u.qiniudn.com/"%dbconfig.qiniuSpace
    def POST(self):
        imgdata=json.loads(web.data())
        with dbconfig.Session() as session:
            user=session.query(datamodel.user.User).filter(datamodel.user.User.uid==imgdata['uid']).first()
            if user is None:
                return json.dumps({"errno":1,"error":"user lost"})
            fileurl=self.SITE+imgdata['hash']
            user.headpic=fileurl
            session.merge(user)
            session.commit()
        return json.dumps({"errno":0,"error":"Success","url":fileurl})

class BackgroundImg(WebSiteBasePage.AutoPage):
    def GET(self):
        params=web.input(usepage='0')
        sessionid=params.get('sessionid',None)
        if sessionid is None:
            return "No Session id"
        data=dbconfig.redisdb.get(str('session:%s'%sessionid))
        if data is None:
            return {"errno":1,"error":"session not found","result":{}}
        data=json.loads(data)
        policy = qiniu.rs.PutPolicy(dbconfig.qiniuSpace)
        policy.callbackUrl='http://%s/upload/BackgroundImgDone'%website_config.hostname
        policy.callbackBody='{"name":"$(fname)","hash":"$(etag)","width":$(imageInfo.width),"height":$(imageInfo.height),' +\
                            '"uid":%d}'%data['uid']
        uptoken = policy.token()
        if int(params['usepage'])==0:
            web.header("Content-type","application/json")
            return json.dumps({'token':uptoken})
        tpl=WebSiteBasePage.jinja2_env.get_template('upload/HeadImg.html')
        return tpl.render(token=uptoken)
    def POST(self):
        pass
class BackgroundImgDone(WebSiteBasePage.AutoPage):
    SITE="http://%s.u.qiniudn.com/"%dbconfig.qiniuSpace
    def POST(self):
        imgdata=json.loads(web.data())
        with dbconfig.Session() as session:
            user=session.query(datamodel.user.User).filter(datamodel.user.User.uid==imgdata['uid']).first()
            if user is None:
                return json.dumps({"errno":1,"error":"user lost"})
            fileurl=self.SITE+imgdata['hash']
            user.background_image=fileurl
            session.merge(user)
            session.commit()
        return json.dumps({"errno":0,"error":"Success","url":fileurl})