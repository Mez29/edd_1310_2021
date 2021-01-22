from Arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)

abb.transversal()
abb.transversal("preorden")
abb.transversal("posorden")
res = abb.search(25)
print(f"El resultado es :{ res }")
abb.remove(35)
abb.transversal()
