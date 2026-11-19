import unittest
from main import audit
class SSHConfigTests(unittest.TestCase):
    def test_risky_options(self):
        issues=audit("Host demo\n  StrictHostKeyChecking no\n  ForwardAgent yes\n")
        self.assertEqual(len(issues),2)
    def test_duplicate_alias(self):
        issues=audit("Host demo\n HostName a\nHost demo\n HostName b\n")
        self.assertTrue(any("Duplicate Host alias" in x["message"] for x in issues))
    def test_safe_config(self):
        self.assertEqual(audit("Host demo\n StrictHostKeyChecking yes\n"),[])
if __name__=="__main__": unittest.main()
