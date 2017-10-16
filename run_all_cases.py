import unittest
import HTMLTestRunner
import time

def all_case():
    case_dir = "D:\\python3\\cjiang01\\cjiangTest01"
    testcases = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    testcases.addTest(discover)
    print(testcases)
    return testcases

if __name__ == '__main__':
    #runner = unittest.TextTestRunner().run(all_case())
    testTime = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    report_path = "D:\\python3\\cjiang01\\TestResult\\" + testTime+ "result.html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'这是我的自动化测试报告',description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()




