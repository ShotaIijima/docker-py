#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docker

class DockerUtil:
    """メール送信を行うためのUtilityクラス"""
    def __init__(self, docker_url):
        self.url = docker_url
