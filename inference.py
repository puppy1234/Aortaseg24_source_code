# -*- coding: utf-8 -*-
import re
import sys
from nnUNet.nnunetv2.inference.predict_from_raw_data import predict_entry_point
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(predict_entry_point())
