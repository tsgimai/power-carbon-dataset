# Power-System Datasets for Nodal Carbon Emission Factor Estimation

Version: 1.0.1

This repository contains the author-supplied simulation data matrices for
nodal carbon emission factor estimation in two power-system cases. The
original data files are distributed without numerical changes.

| File | Case label in the study | Stored matrix | Scenario groups |
|---|---|---|---|
| `data/5000张图.xlsx` | Modified IEEE 123-node case with 114 output rows | 114 × 15000; first worksheet `Sheet1`; no header | 5000 |
| `data/carbon_flow_samples.csv` | IEEE 118-bus case | 118 × 15000; no header | 5000 |

## Matrix organization

Rows are the stored node/output coordinates. Every three consecutive columns
belong to one operating scenario. The supplied 114-row data loader uses the
first two columns of each group as inputs and the third as the prediction
target. The 118-row matrix has the same three-column grouping.

For a zero-based scenario index `s`, the group occupies columns `3*s`,
`3*s+1`, and `3*s+2`. There are no column headers or explicit scenario IDs
in the original matrices. Preserve the stored row and column order.
Physical field definitions, units, and the mapping to bus identifiers should
be read together with the associated study; those metadata are not encoded
as headers in these files. This release does not introduce a new split or
change any historical experiment result.

## Integrity verification

`DATASET_MANIFEST.json` records the file sizes, shapes and SHA-256 checksums.
`SHA256SUMS.txt` provides the same data-file checksums in a standard text form.
Run the dependency-free check from this repository directory:

```shell
python verify_files.py
```

To read the numerical matrices in Python:

```python
import numpy as np
import pandas as pd

a = pd.read_excel("data/5000张图.xlsx", header=None).to_numpy()
b = np.loadtxt("data/carbon_flow_samples.csv", delimiter=",")

# Shapes: scenario × output row × channel
a_groups = a.reshape(a.shape[0], 5000, 3).transpose(1, 0, 2)
b_groups = b.reshape(b.shape[0], 5000, 3).transpose(1, 0, 2)
```

The reading example requires NumPy, pandas and an Excel-reading engine such
as openpyxl. It does not train a model or recompute the reported results.

## Scope and attribution

This is a data release. It does not include a model implementation,
checkpoint, or a claim that the release reproduces every manuscript table.
Please cite this repository version and the associated article when using
the data. The associated article's publication identifier can be added
after publication.
