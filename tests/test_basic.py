
""" Code unit-tests go here. """
import numpy as np
import image_ema_project

def test_roi_xy():
    '''test the roi_xy function'''#为了测试所得到的结果和已经知道的结果是否相同
    xy = np.arange(-4,5)
    result = [xy,xy] #实际已经知道的结果

    roi_xy = image_ema_project.roi_xy([0,0],[8,8]) #计算得到的结果
    
    assert np.all(np.equal(roi_xy,result)) #返回true or false