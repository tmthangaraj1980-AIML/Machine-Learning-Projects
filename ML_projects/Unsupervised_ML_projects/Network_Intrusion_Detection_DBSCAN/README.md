## Conclusion

This project demonstrates an end-to-end implementation of DBSCAN for network intrusion detection using the NSL-KDD dataset.

The workflow included exploratory data analysis, frequency encoding of categorical features, feature scaling, parameter tuning using the K-Distance Graph, DBSCAN clustering, and evaluation of detected anomalies.

Different values of the `eps` parameter were tested to improve clustering performance.

| eps | Total Noise Points | Normal Connections in Noise |
|------|-------------------:|----------------------------:|
| 0.8 | 2766 | 2140 |
| 0.9 | 2326 | 1799 |
| 1.0 | 1990 | 1515 |

The experimental results indicate that **eps = 1.0** provided the best overall performance among the tested values by reducing the number of normal network connections incorrectly identified as anomalies.

This project highlights that DBSCAN is a powerful density-based clustering algorithm for anomaly detection. While the algorithm does not require labeled training data, careful preprocessing and parameter tuning are essential to obtain meaningful results. The project provides a practical demonstration of applying unsupervised machine learning techniques to cybersecurity problems.
