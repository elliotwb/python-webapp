#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' url handlers '
from www.coreweb import get
from www.models import User


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
