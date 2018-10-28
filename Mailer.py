#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Mailer:
    """メール送信を行うためのUtilityクラス"""
    def __init__(self, docker_url):
        self.url = docker_url
