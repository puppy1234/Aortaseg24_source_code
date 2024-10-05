# -*- coding: utf-8 -*-
import re
import sys
from nnUNet.nnunetv2.run.run_training import run_training_entry
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run_training_entry())
