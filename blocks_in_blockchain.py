"""
this script demonstrate how block are created in blockchain and why blockchain are immutable. feel free to reach me if need any assistance.
"""

import hashlib, json

class Block:
    """
    defination of blocks in blockchain
    """
    id = None
    history = None
    parent_id = None
    parent_hash = None

# initiate blockchain transcations
block_A = Block()
block_B = Block()
block_C = Block()

# block_A is genesis node
block_A.id = 1
block_A.history = "rohit you need to create blockchain based personal diary"

# block_B comes into picture and make its own transcation
block_B.id = 2
block_B.history = "sure rohit, we believe you can do it."
block_B.parent_id = block_A.id
block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode("utf-8")).hexdigest()

# now block_C comes into picture
block_C.id = 3
block_C.history = "we are proud of you rohit, you achieved a great feat"
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode("utf-8")).hexdigest()

"""
now lets say if we change any of history or other data that add's up for hash, the subsequent hash will also undergoes changes resulting changes
in all subsequent hash. these hashes are well maintained by other nodes in blockchain and if a block found be different that other then ejected from chain itself.
"""










