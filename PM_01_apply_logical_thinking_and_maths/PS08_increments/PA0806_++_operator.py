# 1.1
#post-increment example

documents = ["Doc1", "Doc2", "Doc3"]
doc_index = 0

while doc_index < len(documents):

    print(documents[doc_index])

    doc_index += 1
print(".............")

# pre-increment example

documents = ["Doc1", "Doc2", "Doc3"]
doc_index = 0

while doc_index < len(documents) - 1:

    doc_index += 1

    print(documents[doc_index])
print(".............")

#1.2
# simulating the loop

n = 10

i = 0

while i < n:

    i += 1  # same as ++i

    print("Picked item:", i)

    i += 1  # loop increment