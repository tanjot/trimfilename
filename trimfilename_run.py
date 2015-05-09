#!/usr/bin/python3
import sys
import trimfilename.main

try:
    sys.exit(trimfilename.main.main())
except KeyboardInterrupt:
    sys.exit(1)