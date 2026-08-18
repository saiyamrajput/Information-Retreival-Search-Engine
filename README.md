Day 1 Findings:

Question: What is Empirical Software-Engineering Research?
Answer: Empirical Software-Engineering research is the study of software development through real-world data, observation, and experiments rather than pure theory.
Question: What is Software-Defect Prediction trying to predict?
Answer: Software-Defect Prediction tries to predict which part of software is most likely to cause error or bugs (like specific files, functions, modules, or individual code block) and therefore cause defect.

3 Data sets that I compared are:
* KC1
* PC1
* CM1

KC1:
Provenance: KC1 is a part of NASA Metrics Data Program. The data represents static code measurements and defect labels from a real-world software system used in storage management in receiving and processing ground data written in C++ programming language.
Target Variable: The Target Variable is ‘defects’ (True for defective, false otherwise).
Size: The dataset contains 2109 rows (Software modules) and 22 columns (21 Explanatory Variable columns and 1 Response Variate column).
Class Balance: Class is Imbalance.
        * Non defective = 1783/2109 = 84.542437 % non-defective rate
        * Defective = 326/2109 = 15.457563 % defective rate
Licensing: This dataset is a publicly distributed data set used extensively in software-defect prediction research with citation/acknowledgment expected and no explicit software license is stated in the supplied ARFF metadata.

CM1:
Provenance: CM1 is a part of NASA Metrics Data Program. The data represents software engineering measurements collected from a NASA spacecraft instrument written in C programming language.
Target Variable: The Target Variable is ‘defects’ (True for defective, false otherwise).
Size: The dataset contains 498 rows (Software modules) and 22 columns (21 Explanatory Variable columns and 1 Response Variate column).
Class Balance: Class is Imbalance.
        * Non defective = 449/498 = 90.160643 % non-defective rate
        * Defective = 49/498 = 9.839357 % defective rate
Licensing: This dataset is a publicly distributed data set used extensively in software-defect prediction research with citation/acknowledgment expected and no explicit software license is stated in the supplied ARFF metadata.

PC1:
Provenance: PC1 is a part of NASA Metrics Data Program. The data represents static source code measurements and defect labels from a flight software for an earth-orbiting satellite written in C programming language.
Target Variable: The Target Variable is ‘defects’ (True for defective, false otherwise).
Size: The dataset contains 1109 rows (Software modules) and 22 columns (21 Explanatory Variable columns and 1 Response Variate column).
Class Balance: Class is Imbalance.
        * Non defective = 1032/1109 = 93.056808 % non-defective rate
        * Defective = 77/1109 = 6.943192 % defective rate
Licensing: This dataset is a publicly distributed data set used extensively in software-defect prediction research with citation/acknowledgment expected and no explicit software license is stated in the supplied ARFF metadata.

Comparison of all 3 datasets:
Attributes / Datasets	KC1	CM1	PC1
Language	C++	C	C
Size	2109 x 22	498 x 22	1109 x 22
Class Balance	Imbalance	Imbalance	Imbalance
Defects	326	49	77
Non-defects	1783	449	1032
Defective rate	15.457563 %	9.839357 %	6.943192
Non-defective rate	84.542437 %	90.160643 %	93.056808 %
Missing Values	0	0	0
Distribution	Positively Skewed	Positively Skewed	Positively Skewed

Conclusion:
The comparison shows that CM1, KC1 and PC1 have a very similar feature structure, with each dataset containing 21 explanatory variables based on static software metrics and one defect target but they differ in dataset size. KC1 is the largest dataset containing 2109 software modules and 326 defective modules, and it also has the highest proportion of defective modules (15.45%), making it the least imbalanced of the three. All three datasets contain no missing values and are positively skewed. Therefore, the three datasets provide a useful range for evaluating a defect-prediction model.


Research Question (RQ): How effectively can software metrics in the KC1 dataset predict whether a software module is defective?
Hypothesis 1 (H1): Machine-learning classifiers using KC1 software metrics will identify defective software modules better than a majority-class baseline.
Hypothesis 2 (H2): Logistic Regression and Random Forest will exhibit different defect-prediction performance when evaluated using the same data split and evaluation protocol.
Hypothesis 3 (H3): Evaluation metrics that focus on the defective class will reveal differences in classifier performance that accuracy alone may obscure.

