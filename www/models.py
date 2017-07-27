#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time,uuid
from www.static.orm import Model,IntegerField,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
# 用户Model
class User(Model):
    __table__ = "users"

    id = StringField(primary_key=True,default=next_id(),ddl='varcher(50)')
    name = StringField(ddl='varcher(50)')
    email = StringField(ddl='varcher(50)')
    passwd = StringField(ddl='varcher(50)')
    admin = BooleanField()
    image = StringField(ddl='varcher(500)')
    created_at = FloatField(default=time.time)
# 博客Model
class Blogs(Model):
    __table__ = "blogs"

    id = StringField(primary_key=True, default=next_id(), ddl='varcher(50)')
    user_id = StringField(ddl='varcher(50)')
    user_name = StringField(ddl='varcher(50)')
    user_image = StringField(ddl='varcher(500)')
    name = StringField()
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

# 评论Model
class Comment(Model):
    __table__ = "comments"
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varcher(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

