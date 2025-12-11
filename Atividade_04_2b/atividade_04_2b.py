class BTreeNode:
    def __init__(self, t, folha=False):
        self.t = t
        self.chaves = []
        self.filhos = []
        self.folha = folha
        self.n = 0

    def search(self, k):
        i = 0
        while i < self.n and k > self.chaves[i]:
            i += 1

        if i < self.n and self.chaves[i] == k:
            return self

        if self.folha:
            return None

        return self.filhos[i].search(k)

    def insert_non_full(self, k):
        i = self.n - 1

        if self.folha:
            self.chaves.append(None)
            while i >= 0 and self.chaves[i] > k:
                self.chaves[i + 1] = self.chaves[i]
                i -= 1
            self.chaves[i + 1] = k
            self.n += 1
        else:
            while i >= 0 and self.chaves[i] > k:
                i -= 1
            i += 1

            if self.filhos[i].n == 2 * self.t - 1:
                self.split_child(i, self.filhos[i])

                if self.chaves[i] < k:
                    i += 1

            self.filhos[i].insert_non_full(k)

    def split_child(self, i, y):
        t = self.t
        z = BTreeNode(t, y.folha)
        z.n = t - 1

        z.chaves = y.chaves[t:(2*t-1)]

        if not y.folha:
            z.filhos = y.filhos[t:(2*t)]

        chave_meio = y.chaves[t-1]

        y.chaves = y.chaves[0:(t-1)]
        if not y.folha:
            y.filhos = y.filhos[0:t]

        y.n = t - 1

        self.filhos.insert(i + 1, z)
        self.chaves.insert(i, chave_meio)
        self.n += 1

    def traverse(self):
        result = []
        for i in range(self.n):
            if not self.folha:
                result.extend(self.filhos[i].traverse())
            result.append(self.chaves[i])

        if not self.folha:
            result.extend(self.filhos[self.n].traverse())

        return result

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}Nível {level}: {self.chaves[:self.n]}")
        if not self.folha:
            for i in range(self.n + 1):
                self.filhos[i].display(level + 1)


class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def search(self, k):
        if self.root is None:
            return None
        return self.root.search(k)

    def insert(self, k):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.chaves.append(k)
            self.root.n = 1
        else:
            if self.root.n == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.filhos.append(self.root)
                s.split_child(0, self.root)

                i = 0
                if s.chaves[0] < k:
                    i += 1
                s.filhos[i].insert_non_full(k)

                self.root = s
            else:
                self.root.insert_non_full(k)

    def traverse(self):
        if self.root is None:
            return []
        return self.root.traverse()

    def display(self):
        if self.root is None:
            print("Árvore vazia")
        else:
            print("=== Estrutura da Árvore B ===")
            self.root.display()


if __name__ == "__main__":
    btree = BTree(3)

    print("=== INSERÇÃO NA ÁRVORE B ===\n")
    values = [10, 20, 5, 6, 12, 30, 7, 17, 3, 15, 25, 40, 45]

    for val in values:
        print(f"Inserindo: {val}")
        btree.insert(val)
        print(f"Percurso: {btree.traverse()}\n")

    btree.display()

    print("\n=== PERCURSO EM ORDEM ===")
    print("Valores ordenados:", btree.traverse())

    print("\n=== BUSCA ===")
    test_values = [15, 8, 30, 45, 1, 20]
    for val in test_values:
        result = btree.search(val)
        if result:
            print(f"Buscar {val}: Encontrado no nó {result.chaves}")
        else:
            print(f"Buscar {val}: Não encontrado")