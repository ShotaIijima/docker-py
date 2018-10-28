#!/usr/bin/env python
# -*- coding: utf-8 -*-

import DockerUtil
import Mailer
from config import config

def main():
    print config["docker"]["url"]

if __name__ == "__main__":
    main()
