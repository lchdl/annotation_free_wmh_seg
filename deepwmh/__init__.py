from __future__ import absolute_import
from .info import __version__, __date__

print('')
print('Please cite the following paper(s) when using the code:')
print('')
print('[1] Chenghao Liu, Zhizheng Zhuo, Liying Qu, Ying Jin, Tiantian Hua, Jun Xu, '
      'Guirong Tan, Yuna Li, Yunyun Duan, Tingting Wang, Zaiqiang Zhang, Yanling Zhang, '
      'Rui Chen, Pinnan Yu, Peixin Zhang, Yulu Shi, Jianguo Zhang, Decai Tian, '
      'Runzhi Li, Xinghu Zhang, Fudong Shi, Yanli Wang, Jiwei Jiang, Aaron Carass, '
      'Yaou Liu, Chuyang Ye. "DeepWMH: a deep learning tool for accurate white matter '
      'hyperintensity segmentation without requiring manual annotations for training". '
      'Science Bulletin, 2023.')
print('[2] Chenghao Liu, Xiangzhu Zeng, Kongming Liang, Yizhou Yu, Chuyang Ye. '
      '"Improved Brain Lesion Segmentation with Anatomical Priors from Healthy Subjects". '
      'Medical Image Computing and Computer Assisted Intervention (MICCAI), 2021.')
print('')
print('If you have any question or found any bug in the code, please open an issue or '
      'a pull request at https://github.com/lchdl/DeepWMH.')
print('')

print('')
print('*    DeepWMH Segmentation Toolbox    *')

_s = 'Version %s (%s)' % (__version__, __date__)
_t = len('    DeepWMH Segmentation Toolbox    ')
_l = (_t - len(_s))//2
_r = _t - len(_s) - _l

if _l < 0 : _l = 0
if _r < 0 : _r = 0

print('* %s%s%s *' % (' '*_l, _s, ' '*_r))
print('')
print('')

from . import *

