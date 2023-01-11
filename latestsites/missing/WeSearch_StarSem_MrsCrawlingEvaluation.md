{% raw %}Results on SSD

|                     |              |     |     |       |       |       |                    |     |     |       |       |       |
|---------------------|:------------:|:---:|:---:|:-----:|:-----:|:-----:|:------------------:|:---:|:---:|:-----:|:-----:|:-----:|
|                     | Exact Scopes |     |     |       |       |       | Token in/out-scope |     |     |       |       |       |
| Method              |      TP      | FP  | FN  |   P   |   R   |  F1   |         TP         | FP  | FN  |   P   |   R   |  F1   |
| Baseline            |      61      |  0  | 107 | 100.0 | 36.31 | 53.28 |        1168        | 537 | 180 | 68.50 | 86.65 | 76.51 |
| C&J ranker          |     115      |  0  | 53  | 100.0 | 68.45 | 81.27 |        1168        | 197 | 180 | 85.57 | 86.65 | 86.11 |
| MRS crawling        |      69      |  0  | 99  | 100.0 | 41.07 | 58.23 |        789         | 71  | 559 | 91.74 | 58.53 | 71.47 |
| MRS + ranker b/off  |      94      |  0  | 74  | 100.0 | 55.95 | 71.75 |        1074        | 151 | 274 | 87.67 | 79.67 | 83.48 |
| Oracle              |     141      |  0  | 27  | 100.0 | 83.93 | 91.26 |        1204        | 38  | 144 | 96.94 | 89.32 | 92.97 |
|                     |              |     |     |       |       |       |                    |     |     |       |       |       |
| MRS + ranker aug-27 |     104      |  0  | 64  | 100.0 | 61.90 | 76.47 |        1086        | 158 | 262 | 87.30 | 80.56 | 83.79 |
| MRS if P &gt;= 0.5  |     116      |  0  | 52  | 100.0 | 69.05 | 81.69 |        1160        | 173 | 188 | 87.02 | 86.05 | 86.53 |
| oracle aug-27       |     141      |  0  | 27  | 100.0 | 83.93 | 91.26 |        1204        | 38  | 144 | 96.94 | 89.32 | 92.97 |

Results on SST, as reported by the official shared task evaluation
script.

|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
|--------------------------|:------------:|:---:|:---:|:------:|:-----:|:-----:|:------------------:|:----:|:----:|:-----:|:-----:|:-----:|
|                          | Exact Scopes |     |     |        |       |       | Token in/out-scope |      |      |       |       |       |
| Method                   |      TP      | FP  | FN  |   P    |   R   |  F1   |         TP         |  FP  |  FN  |   P   |   R   |  F1   |
| Baseline                 |     289      |  6  | 598 | 97.97  | 32.58 | 48.90 |        6438        | 3411 | 491  | 65.37 | 92.91 | 76.74 |
| C&J rules                |     636      |  0  | 251 | 100.0  | 71.70 | 83.52 |        6514        | 1207 | 415  | 84.37 | 94.01 | 88.93 |
| C&J ranker               |     661      |  0  | 226 | 100.0  | 74.52 | 85.40 |        6512        | 983  | 417  | 86.88 | 93.98 | 90.29 |
| " (sst only)             |     659      |  0  | 228 | 100.0  | 74.30 | 85.26 |        6462        | 950  | 467  | 87.18 | 93.26 | 90.12 |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| Aug-12-2013              |              |     |     |        |       |       |                    |      |      |       |       |       |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| MRS crawling             |     350      |  2  | 537 | 99.43  | 39.46 | 56.50 |        4399        | 673  | 2530 | 86.73 | 63.49 | 73.31 |
| \+ baseline              |     420      |  8  | 467 | 98.13  | 47.35 | 63.88 |        6014        | 1735 | 915  | 77.61 | 86.79 | 81.94 |
| \+ C&J rules             |     503      |  2  | 384 | 99.60  | 56.71 | 72.27 |        5997        | 1061 | 932  | 84.97 | 86.55 | 85.75 |
| \+ C&J ranker            |     516      |  2  | 371 | 99.61  | 58.17 | 73.45 |        6033        | 1022 | 896  | 85.51 | 87.07 | 86.28 |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| Oracle                   |     698      |  0  | 189 | 100.0  | 78.69 | 88.08 |                    |      |      |       |       |       |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| Aug-23-2013 \[1212/pet\] |              |     |     |        |       |       |                    |      |      |       |       |       |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| MRS crawling             |     411      |  2  | 476 | 99.52  | 46.34 | 63.24 |        4576        | 668  | 2353 | 87.26 | 66.04 | 75.18 |
| \+ C&J ranker            |     554      |  2  | 333 | 99.64  | 62.46 | 76.79 |        6049        | 953  | 880  | 86.39 | 87.30 | 86.84 |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| Aug-23-2013 \[1212/ace\] |              |     |     |        |       |       |                    |      |      |       |       |       |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| MRS crawling             |     418      |  4  | 469 | 99.05  | 47.13 | 63.87 |        4760        | 749  | 2169 | 86.40 | 68.70 | 76.54 |
| \+ C&J ranker            |     545      |  4  | 342 | 99.27  | 61.44 | 75.90 |        6063        | 1012 | 866  | 85.70 | 87.50 | 86.59 |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| crawl if P &gt;= 0.5     |              |     |     |        |       |       |                    |      |      |       |       |       |
| MRS + C&J ranker         |     646      |  0  | 241 | 100.00 | 72.83 | 84.28 |        6470        | 960  | 459  | 87.08 | 93.38 | 90.12 |
|                          |              |     |     |        |       |       |                    |      |      |       |       |       |
| Aug-27-2013 Oracle       |     783      |  0  | 104 | 100.00 | 88.28 | 93.78 |        6685        | 240  | 244  | 96.53 | 96.48 | 96.50 |

|                          |     |     |     |       |       |       |      |      |      |       |       |       |
|:------------------------:|:---:|:---:|:---:|:-----:|:-----:|:-----:|:----:|:----:|:----:|:-----:|:-----:|:-----:|
|                          |     |     |     |       |       |       |      |      |      |       |       |       |
| Aug-27-2013 \[1212/ace\] |     |     |     |       |       |       |      |      |      |       |       |       |
|                          |     |     |     |       |       |       |      |      |      |       |       |       |
|       MRS crawling       | 448 |  4  | 439 | 99.12 | 50.51 | 66.92 | 4847 | 766  | 2082 | 86.35 | 69.95 | 77.29 |
|      \+ C&J ranker       | 575 |  4  | 312 | 99.31 | 64.83 | 78.45 | 6150 | 1029 | 779  | 85.67 | 88.76 | 87.19 |

Notes:

- Errors in exact scope count just once, as a false negative. During
the shared task there was some debate as to whether an error should
generate both an FP and an FN, but this seemed to be the organisers'
preference.
- Subsequent results for MRS crawling indicate the results of using
the predictions of the specified method for cases where no
prediction is made by the MRS crawling rules.
- The 1212/ace profile differs from the 1212/pet profile in the
processor used for parsing. The most important intentional
difference is that the resource limit under ACE is relatively vast
(only six sentences hit resource limits), so grammar coverage was
slightly higher.

Last update: 2013-08-28 by WoodleyPackard [[edit](https://github.com/delph-in/docs/wiki/WeSearch_StarSem_MrsCrawlingEvaluation/_edit)]{% endraw %}