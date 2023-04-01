import numpy as np
def remove_invalid(arrays: list[np.ndarray]) -> list[np.ndarray]:
    """
    Remove NaNs, Infs and Zeros from a list of numpy arrays.

    :param arrays: A list of numpy arrays.
    :return: A new list of numpy arrays without NaNs, Infs and Zeros.
    :raises ValueError: If the input list is empty.

    Example:

    >>> x = np.array([0, np.nan, 1, 2, np.inf])
    >>> y = np.array([1, 2, 3, 4, 5])
    >>> z = np.array([0, 0, 0, 0, 0])
    >>> arrays = [x, y, z]
    >>> filtered_arrays = remove_invalid(arrays)
    >>> np.array_equal(filtered_arrays[0], np.array([1, 2]))
    True
    >>> np.array_equal(filtered_arrays[1], np.array([1, 2, 3, 4, 5]))
    True
    >>> np.array_equal(filtered_arrays[2], np.array([], dtype=np.int64))
    True
    """
    if not arrays:
        raise ValueError("The input list must not be empty.")

    # Remove empty arrays from the input list
    arrays = [array for array in arrays if len(array) > 0]

    if not arrays:
        raise ValueError("The input list must contain at least one non-empty numpy array.")

    new_arrays = []
    for array in arrays:
        # Remove NaNs, Infs and Zeros from the array
        valid_mask = ~(np.isnan(array) | np.isinf(array) | (array == 0))
        filtered_array = array[valid_mask]
        new_arrays.append(filtered_array)

    if all(len(a) == 0 for a in new_arrays):
        raise ValueError("The input list contains only empty numpy arrays.")

    return new_arrays


