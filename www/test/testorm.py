#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from www.static.been import User
from www.static.orm import create_pool
import asyncio



async def test_save():
    user = User(id=3, name="Caisw")
    await user.save()


async def test_find():
    user = await User.findAll()
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop,user="root",db="test"))
# loop.run_until_complete(test_save())
loop.run_until_complete(test_find())
