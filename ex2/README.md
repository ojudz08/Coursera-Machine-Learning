# Logistic Regression

Logistic regression is  mostly used for classification tasks (i.e. classifying spam emails, malignant or benign tumors). 

## Logistic Function (Sigmoid Function) 

We want our predicted model to have a value of between 0 and 1. 

<img src="https://latex.codecogs.com/svg.image?{\color{white}0\leq{h}_{\theta}(x)\leq&space;1" title="https://latex.codecogs.com/svg.image?0\leq{h}_{\theta}(x)\leq 1" />

In order to achieve this, we use the sigmoid function.

<img src="https://latex.codecogs.com/svg.image?{\color{white}g(z)=\frac{1}{1&plus;e^{-z}}" title="https://latex.codecogs.com/svg.image?g(z)=\frac{1}{1+e^{-z}}" />


![Sigmoid](/img/sigmoid.PNG?raw=true "Sigmoid")


The hypothesis will look like this

<img src="https://latex.codecogs.com/svg.image?{\color{white}h=g(z)" title="https://latex.codecogs.com/svg.image?h=g(z)" />