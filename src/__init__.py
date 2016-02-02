import wx as gui
import multiprocessing.dummy as mthread
import subprocess
import sys as python
import os as platform
import pprint as pp
import re as norm
import traceback as tb

nl = lambda s: s+platform.linesep #new line

__all__ = ['view',
           'cmd',
           'ssh',
           'pick',
           'pipe',
           'start']
