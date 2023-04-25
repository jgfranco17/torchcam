import torch
import pytest
from .conftest import basic_tensor


def test_torch_tensor_creation(basic_tensor):
    """
    Verify the creation of PyTorch tensors.
    """
    assert basic_tensor.shape == (3, 224, 224), "Incorrect tensor shape"
    assert basic_tensor.dtype == torch.float32, "Incorrect tensor type"
    assert torch.min(basic_tensor) >= -1.0, "Tensor values outside of range"
    assert torch.max(basic_tensor) <= 1.0, "Tensor values outside of range"


def test_tensor_multiplication():
    """
    Verify the operations of PyTorch tensors
    """
    tensor1 = torch.randn((3, 224, 224))
    tensor2 = torch.randn((3, 224, 224))
    tensor_product = tensor1 * tensor2

    assert tensor_product.shape == (3, 224, 224), "Incorrect tensor shape"
    assert tensor_product.dtype == torch.float32, "Incorrect tensor type"


def test_tensor_construction():
    """
    Check the generation of new tensors from Python built-ins
    """
    tensor = torch.tensor([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    assert tensor.shape == (3, 3), "Incorrect tensor shape"
    assert tensor.dtype == torch.int64, "Incorrect tensor type"
