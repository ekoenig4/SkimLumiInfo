#!/usr/bin/env python
import os
import sys
cmssw = os.getenv("CMSSW_BASE")

from CondorTools.SubmitDataset import submit,options
options['year'] = '2017'
options['region'] = 'LM'
# options['parallel'] = True
# options['submit'] = False
#----Submit---#
# submit('met',sub='D',script='skimLumi.py',filelist=True)
submit('met_crab',sub='D',script='skimLumi.py',filelist=True)

