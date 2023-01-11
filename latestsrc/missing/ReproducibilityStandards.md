{% raw %}In order to facilitate comparison with and reproducibility of
experiments using DELPH-IN data and tool sets, this page documents
standard training and testing data sets for each grammar, and standard
evaluation metrics and terminology. We encourage everyone to use the
standards listed here, or to describe any deviations in terms of these
standards.

## Data

- ErgDataSets
- JacyDataSets
- GgDataSets
- SrgDataSets
- KrgDataSets
- LxDataSets
- WambayaDataSets
- CheetahDataSets

## Evaluation Metrics

### Coverage

- observed coverage: percentage of items that received at least one
parse
- verified coverage: percentage of items for which a gold standard
analysis was found during treebanking

### Accuracy

It is important to specify whether these metrics are calculated over:

- all items in a data set
- all items that have a gold standard analysis
- all items that received a parse
- the intersection of the last two

#### metrics

- exact match: percentage of items for which the top analysis was the
gold analysis
- ElementaryDependencyMatch
- DMRS
<update date omitted for speed>{% endraw %}