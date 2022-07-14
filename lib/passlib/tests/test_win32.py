"""tests for passlib.win32 -- (c) Assurance Technologies 2003-2009"""
#=============================================================================
# imports
#=============================================================================
# core
import warnings
# site
# pkg
from lib.passlib.tests.utils import TestCase
# module
from lib.passlib.utils.compat import u

#=============================================================================
#
#=============================================================================
class UtilTest(TestCase):
    """test util funcs in passlib.win32"""

    ##test hashes from http://msdn.microsoft.com/en-us/library/cc245828(v=prot.10).aspx
    ## among other places

    def setUp(self):
        super(UtilTest, self).setUp()
        warnings.filterwarnings("ignore",
                                "the 'passlib.win32' module is deprecated")

    def test_lmhash(self):
        from lib.passlib.win32 import raw_lmhash
        for secret, hash in [
            ("OLDPASSWORD", u("c9b81d939d6fd80cd408e6b105741864")),
            ("NEWPASSWORD", u('09eeab5aa415d6e4d408e6b105741864')),
            ("welcome", u("c23413a8a1e7665faad3b435b51404ee")),
            ]:
            result = raw_lmhash(secret, hex=True)
            self.assertEqual(result, hash)

    def test_nthash(self):
        warnings.filterwarnings("ignore",
                                r"nthash\.raw_nthash\(\) is deprecated")
        from lib.passlib.win32 import raw_nthash
        for secret, hash in [
            ("OLDPASSWORD", u("6677b2c394311355b54f25eec5bfacf5")),
            ("NEWPASSWORD", u("256781a62031289d3c2c98c14f1efc8c")),
            ]:
            result = raw_nthash(secret, hex=True)
            self.assertEqual(result, hash)

#=============================================================================
# eof
#=============================================================================
