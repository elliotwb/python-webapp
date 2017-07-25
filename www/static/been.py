#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from www.static.orm import Model,IntegerField,StringField


class User(Model):
    __table__ = "user"

    id = IntegerField(primary_key=True)
    name = StringField()






