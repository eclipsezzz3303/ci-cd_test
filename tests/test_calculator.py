import sys                                                                                                                                                       
import os                                                                                                                                                        
                                                                                                                                                                
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))                                                                                         
                                                                                                                                                                
from calculator import add, subtract                                                                                                                             
                                                                                                                                                                
                                                                                                                                                                
def test_add():                                                                                                                                                  
    assert add(2, 3) == 6                                                                                                                                        

                                                                                                                                                           
                                                                                                                                                                
def test_subtract():                                                                                                                                             
    assert subtract(5, 3) == 2     