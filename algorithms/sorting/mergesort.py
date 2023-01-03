"""Module with the implementation of the MergeSort algorithm."""

from .sort import Sort


class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self, items):
        if len(items) <= 1:
            return items

        sorted_items = items.copy()
        chunk_size = 1
        while chunk_size < len(sorted_items):

            i = 0
            while i < len(sorted_items):
                mid = i + chunk_size
                j = min(i + 2 * chunk_size, len(sorted_items))
                sorted_items[i:j] = self._merge(sorted_items[i:mid], sorted_items[mid:j])

                i += chunk_size * 2

            chunk_size = chunk_size * 2

        return sorted_items

    def _merge(self, left, right):
        merged = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if self._comp_func(left[left_idx], right[right_idx]):
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        while left_idx < len(left):
            merged.append(left[left_idx])
            left_idx += 1

        while right_idx < len(right):
            merged.append(right[right_idx])
            right_idx += 1

        return merged
