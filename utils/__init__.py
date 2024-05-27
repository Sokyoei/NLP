import numpy as np
import torch
from torch import Tensor
from numpy import ndarray
import torch.nn.functional as F


def one_hot_encode(data: ndarray | Tensor, max_len: int):
    if isinstance(data, ndarray):
        return np.eye(max_len, dtype=np.float32)[data]
    elif isinstance(data, Tensor):
        return F.one_hot(data, max_len)
    else:
        raise f"{type(data)} 不支持。"
