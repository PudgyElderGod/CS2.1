from Prefix_Tree_Node import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node = self.root

        for i in string:
            # check if i is child of cur node
            if node.has_child(i):
                child = node.get_child(i)
                node = child
                # set is as child
            else:
                # are we at the end
                return node.is_terminal()

        return node.is_terminal()

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        cur = self.root

        for i in string:
            if not cur.has_child(i):
                new_node = PrefixTreeNode(i)
                cur.add_child(i, new_node)
                cur = new_node
            else:
                if cur.has_child(i):
                    cur = cur.get_child(i)

        if not cur.is_terminal():
            self.size += 1
            cur.terminal = True

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        if len(string) == 0:
            return self.root, 0

        node = self.root

        index = 0
        while index < len(string) and node.has_child(string[index]) is True:
            node = node.get_child(string[index])
            index += 1
        return node, index

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        completions = []

        if prefix == '':
            return self.strings()
        node = self._find_node(prefix)
        if node[0].character != '':
            self._traverse(node[0], prefix, completions.append)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        all_strings = []
        self._traverse(self.root, '', all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        if node.is_terminal():
            visit(prefix)
        for i in node.children.keys():
            child = node.get_child(i)
            self._traverse(child, prefix + i, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    tongue_twisters = {
        'Seashells': 'Peter Piper picked a patch of pickled peppers'.split(),
    }
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()