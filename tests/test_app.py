import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app

def test_add():
    assert app.add(2, 3) == 5
