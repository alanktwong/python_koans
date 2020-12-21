#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Duck:
    def __init__(self):
        # Genius!
        self._password = 'password'

    @property
    def name(self):
        return "Daffy"
