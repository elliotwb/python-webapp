#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from www.static.orm import create_pool
from www.static.models import User,Blogs,Comment
import asyncio

async def test_save():
    # u = User(name="Test1", email="test1@163.com", passwd="66666666", image="about:blank")
    u = User(name='Test2', email='test2@163.com', passwd='88888888', image='about:blank')
    await u.save()

async def test_findall():
    user = await User.findAll()
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop,user="root",db="webapp"))
# loop.run_until_complete(test_save())
loop.run_until_complete(test_findall())




