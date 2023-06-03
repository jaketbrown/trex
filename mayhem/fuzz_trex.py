#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers
import sre_parse

with atheris.instrument_imports():
    import trrex
    import re
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        pattern = trrex.make(fuzz_helpers.build_fuzz_list(fdp, [str]))
        re.findall(pattern, fdp.ConsumeRemainingString())
    except sre_parse.error:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()