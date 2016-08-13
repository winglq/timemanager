from unittest import TestCase
import unittest
import mock
import timemanager
from configure import Cfg

class TimeManager(TestCase):
    @mock.patch.object(timemanager.ProtectEye, 'initialize')
    @mock.patch.object(timemanager.ProtectEye, 'DestroyAfterSleep')
    def test_on_button_click(self, call_back, init,
                             ):
        cfg = Cfg()
        cfg.small_break_count = 5
        p = timemanager.ProtectEye(None, cfg)
        p.labelVariable = mock.MagicMock()
        p.button = mock.MagicMock()
        p.buttondelay = mock.MagicMock()
        p.OnButtonClick()
        self.assertTrue(init.called_once)
        self.assertTrue(call_back.called_once)
        self.assertEqual(1, p.small_break_count)
        for i in range(5):
            p.OnButtonClick()
        self.assertEqual(0, p.small_break_count)

if __name__ == '__main__':
    unittest.main()
    
