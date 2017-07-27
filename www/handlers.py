#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from www.coreweb import get
from www.models import User, Blogs


# @get('/')
# async def index(request):
#     users = await User.findAll()
#     return {
#         '__template__': 'test.html',
#         'users': users
#     }

@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blogs(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blogs(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blogs(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }



