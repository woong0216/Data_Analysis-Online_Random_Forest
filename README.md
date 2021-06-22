# Data Analysis using Online Random Forest

## Propose
- When collecting real-time data, we would like to implement how accuracy.

## Dataset
- Rotating Hyperplane Dataset

![Rotating Hyperplane Dataset](https://user-images.githubusercontent.com/63955072/122891592-98098480-d37f-11eb-8b0c-209ef46e7cec.PNG)

- Dataset 1 (Hyperplane 3)

![Dataset 1](https://user-images.githubusercontent.com/63955072/122891643-a2c41980-d37f-11eb-9393-3c5c01a1c298.png)

- Dataset 2 (Hyperplane 6)

![Dataset 2](https://user-images.githubusercontent.com/63955072/122891685-abb4eb00-d37f-11eb-8030-d2736dc5a410.png)

## Method
- It was applied to enable adaptive learning through Incremental Tree Building.
- The parameter specifies warm_start as True, which has the most similar effect. (Like Online Random Forest)

## Analysis
- Dataset 1 Result (Hyperplane 3)
> Accuracy: 84.58% <br/>

![Dataset 1 result](https://user-images.githubusercontent.com/63955072/122892333-41e91100-d380-11eb-95bc-3629186ee0a8.png)

- Dataset 2 Result (Hyperplane 6)
> Accuracy: 85.22% <br/>

![Dataset 2 result](https://user-images.githubusercontent.com/63955072/122892531-6e9d2880-d380-11eb-99f5-0210a11d662e.png)

## Conclusion
- As a result of the study, gradual concept drift was confirmed.
- The concept drift was consistent with the motion of the variables that occurred and the appearance of significant variables in feature importance.
