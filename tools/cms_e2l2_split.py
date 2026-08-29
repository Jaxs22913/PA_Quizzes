"""Which Lecture 11 items belong to the OBJECTIVE set rather than the vignettes.

They were authored into the vignette pool, but they are pure pathway-and-anatomy
recall -- "where do the first-order sympathetic neurons synapse" cannot take a
patient without inventing one, and the exam standard measures a vignette set by
whether its stems carry an explicit age. Rather than delete good questions, they
are tagged here and the partitioner routes them: the vignette sets exclude them,
the objective sets use them.

Indices are into POOL_A + POOL_B + POOL_C of cms_e2l2_vig_{a,b,c}.
"""
RECALL = {14, 16, 29, 32, 33, 34, 35, 36, 37, 38, 39, 40, 44, 47, 51, 55, 56, 58}
