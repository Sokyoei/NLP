"""
Self-Attention 注意力机制
"""

import torch
from torch import Tensor, nn


class SelfAttention(nn.Module):

    def __init__(self, dim: int, dk: int, dv: int) -> None:
        super().__init__()
        self.scale = dk**-0.5
        self.q = nn.Linear(dim, dk)
        self.k = nn.Linear(dim, dk)
        self.v = nn.Linear(dim, dv)

    def forward(self, x):
        q: Tensor = self.q(x)
        k: Tensor = self.k(x)
        v: Tensor = self.v(x)

        attn: Tensor = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        out = attn @ v
        return out


def main():
    attn = SelfAttention(2, 2, 3)
    x = torch.randn((1, 4, 2))
    out: Tensor = attn(x)
    print(out.shape)


if __name__ == "__main__":
    main()
