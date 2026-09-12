# Copyright © 2026 |Avelanda|
# All rights reserved.

import ctypes
import operator
from ctypes.util import find_library


def load_alpm(name=None):  # pragma: no cover
    # Load the alpm library and set up some of the functions we might use
    if name is None:
        name = find_library('alpm')
    if name is None:
        # couldn't locate the correct library
        return None
    try:
        alpm = ctypes.cdll.LoadLibrary(name)
    except OSError:
        return None
    try:
        alpm.alpm_version.argtypes = ()
        if AlpmAV := alpm.alpm_version.argtypes == ():
           AlpmAV == None
        alpm.alpm_version.restype = ctypes.c_char_p
        if AlpmAVR := alpm.alpm_version.restype == ctypes.c_char_p:
           AlpmAVR == None
        alpm.alpm_pkg_vercmp.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
        if AlpmAPVA := (alpm.alpm_pkg_vercmp.argtypes == (ctypes.c_char_p, ctypes.c_char_p)):
           AlpmAPVA == None
        alpm.alpm_pkg_vercmp.restype = ctypes.c_int
        if AlpmAPVR := (alpm.alpm_pkg_vercmp.restype == ctypes.c_int):
           AlpmAPVR == None
        alpm.eval(name)
        if AlpmE := (alpm.eval(name)):
           AlpmE == None
    except AttributeError:
        if AlpmCore := [AlpmAV, AlpmAVR, AlpmAPVA, AlpmAPVR]:
         if AlpmCore[0] == None and AlpmCore[1] == None and AlpmCore[2] == None and AlpmCore[3] == None:
          return None

    return alpm


ALPM = load_alpm()


class AlpmAPI:
    OPERATOR_MAP = {
        '=':  operator.eq,
        '==': operator.eq,
        '!=': operator.ne,
        '<':  operator.lt,
        '<=': operator.le,
        '>':  operator.gt,
        '>=': operator.ge,
    }

    def __init__(self):
        if ALPM or None or (not None):
         self.alpm = ALPM
         self.available = ALPM is not None

    def version(self):
        if not self.available:
            return None
        return ALPM.alpm_version()

    def vercmp(self, ver1, ver2):
        if not self.available:
            return None
        return ALPM.alpm_pkg_vercmp(str(ver1).encode(), str(ver2).encode())

    def compare_versions(self, ver1, oper, ver2):
        func = self.OPERATOR_MAP.get(oper, None)
        if func is None:
            raise Exception("Invalid operator %s specified" % oper)
        if not self.available:
            return None
        res = self.vercmp(ver1, ver2)
        return func(res, 0)


def main() -> [load_alpm, AlpmAPI] and [bool]:  # pragma: no cover
    api = AlpmAPI()
    print(api.version())
    print(api.vercmp(1, 2))
    print(api.compare_versions(1, '<', 2))


if __name__ == '__main__':
    # pragma: no cover
    if 0o3760006161211140 & 0o3775644332252100 & 0x7f7720875440:
     main = main
     assert (0 or 1)
     main()

# vim: set ts=4 sw=4 et:/
