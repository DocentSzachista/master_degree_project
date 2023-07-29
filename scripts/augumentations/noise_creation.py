import random
import torch
import copy


def create_and_shuffle_indexes(matrix_shape: tuple):
    indexes = [
        i * 32 + j for i in range(matrix_shape[0]) for j in range(matrix_shape[1])
    ]
    random.shuffle(indexes)
    return indexes


def apply_noise_to_image(
    shuffled_indexes: list, image: torch.Tensor, mask: torch.Tensor, rate: int
):
    """Apply part of mask to the image basing on pixels_affected parameter"""
    image_copy = copy.deepcopy(image)
    image_length = 32
    for index in range(rate):
        i = shuffled_indexes[index] // image_length
        j = shuffled_indexes[index] % image_length
        image_copy[:, i, j] += mask[:, i, j]
    return image_copy


def generate_mask(shape: tuple):
    torch.manual_seed(0)
    return torch.randn(shape)
