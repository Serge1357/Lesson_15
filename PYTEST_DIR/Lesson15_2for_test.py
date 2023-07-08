from binarytree import *
import random
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Прямий обхід
    def travers_pre_order(self):
        print(self.val, end=" ")
        if self.left:
            self.left.travers_pre_order()
        if self.right:
            self.right.travers_pre_order()

    # Зворотній обхід
    def travers_in_order(self):
        if self.left:
            self.left.travers_in_order()
        print(self.val, end=" ")
        if self.right:
            self.right.travers_in_order()

    # Додавання нового елементу
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Node(key)
                return
    #-------------------------------------------------------------------------------
    def add_list(self, lst):
        for i in lst:
            self.insert(i)

    def tree_max(self):
        if self.right is None:
            return self.val
        return self.right.tree_max()

    def tree_min(self):
        if self.left is None:
            return self.val
        return self.left.tree_min()

    def delete(self, key):
        if not self:
            return self
        if self.val > key:
            self.left = self.left.delete(key)
        elif self.val < key:
            self.right= self.right.delete(key)
        else:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            temp_val = self.right
            mini_val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.val
            self.val = mini_val
            self.right = self.right.delete(self.val)
        return self
    #--------------------------------------------------------------------------------
    # Друк дерева
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


a = Node(10)
lst = [5,8,13,3,0,6,-8,4,7,12,15,16]
a.add_list(lst)
a.display()
print("max:",a.tree_max())
print("min:",a.tree_min())
a.delete(10)
a.display()