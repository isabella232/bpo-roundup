#! /usr/bin/env python

# $Id: setup.py,v 1.4 2001-07-27 07:20:17 richard Exp $

from distutils.core import setup, Extension
from distutils.util import get_platform

from glob import glob
import os

templates = 'classic', 'extended'
packagelist = [ 'roundup', 'roundup.backends', 'roundup.templates' ]
installdatafiles = []

for t in templates:
    packagelist.append('roundup.templates.%s'%t)
    packagelist.append('roundup.templates.%s.detectors'%t)
    tfiles = glob(os.path.join('roundup','templates', t, 'html', '*'))
    tfiles = filter(os.path.isfile, tfiles)


setup ( name = "roundup", 
	version = "0.2.0",
	description = "roundup tracking system",
	author = "Richard Jones",
	author_email = "richard@sourceforge.net",
	url = 'http://sourceforge.net/projects/roundup/',
	packages = packagelist,
    scripts = ['roundup-admin', 'roundup-mailgw', 'roundup-server']
)

# now install the bin programs, and the cgi-bin programs
# not sure how, yet.

#
# $Log: not supported by cvs2svn $
# Revision 1.3  2001/07/27 06:56:25  richard
# Added scripts to the setup and added the config so the default script
# install dir is /usr/local/bin.
#
# Revision 1.2  2001/07/26 07:14:27  richard
# Made setup.py executable, added id and log.
#
#
