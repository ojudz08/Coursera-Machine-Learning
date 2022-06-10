# Linear Regression (1 Variable)

Linear regression is a type of regression model that assumes a linear relationship between the independent variable (x) and the dependent variable (y). 

## Linear Regression (1 Variable)


## Hypothesis

A simple linear regression is in the form of

<img src="https://latex.codecogs.com/svg.image?{\color{white}h_{\theta}(x)=\theta_{0}&plus;\theta_{1}x" title="https://latex.codecogs.com/svg.image?h_{\theta}(x)=\theta_{0}+\theta_{1}x" />

where:

<img src="https://latex.codecogs.com/svg.image?{\color{white}h_{\theta}(x)\text{&space;&space;is&space;the&space;dependent&space;variable&space;y}" title="https://latex.codecogs.com/svg.image?h_{\theta}(x)\text{ is the dependent variable y}" />

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta_0\text{&space;and&space;}\theta_1\text{&space;&space;are&space;the&space;parameters&space;or&space;coefficients}" title="https://latex.codecogs.com/svg.image?\theta_0\text{ and }\theta_1\text{ are the parameters or coefficients}" />

<img src="https://latex.codecogs.com/svg.image?{\color{white}x\text{&space;is&space;the&space;independent&space;variable&space;x}&space;" title="https://latex.codecogs.com/svg.image?x\text{ is the independent variable x} " />


## Cost Function

To figure out the best possible values for theta that would provide the best fit line for the data, minimize the error between the predicted value and actual value.

<img src="https://latex.codecogs.com/svg.image?{\color{white}J(\theta_{0},\theta_{1})=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2" title="https://latex.codecogs.com/svg.image?J(\theta_{0},\theta_{1})=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}(x^{(i)})-y^{(i)})^2" />

And the goal is to:

<img src="https://latex.codecogs.com/svg.image?{\color{white}\underset{{\theta_0},{\theta_1}}{minimize}=J({\theta_0},{\theta_1})" title="https://latex.codecogs.com/svg.image?\underset{{\theta_0},{\theta_1}}{minimize}=J({\theta_0},{\theta_1})" />


## Gradient Descent

The method of updating the parameters to reduce the cost function. This is done by initializing the parameters theta and change these values iteratively to reduce cost.

<img src="https://latex.codecogs.com/svg.image?{\color{white}{\theta_j}:={\theta_j}-{\alpha}\frac{\delta}{\delta\theta_j}J({\theta_0},{\theta_1})" title="https://latex.codecogs.com/svg.image?{\theta_j}:={\theta_j}-{\alpha}\frac{\delta}{\delta\theta_j}J({\theta_0},{\theta_1})" />

So the corresponding gradient descent algorithm for theta parameters

<img src="https://latex.codecogs.com/svg.image?{\color{white}{\theta_0}:={\theta_0}-{\alpha}\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})" title="https://latex.codecogs.com/svg.image?{\theta_0}:={\theta_0}-{\alpha}\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})" />


<img src="https://latex.codecogs.com/svg.image?{\color{white}{\theta_1}:={\theta_1}-{\alpha}\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})\text{&space;&space;}\cdot\text{&space;&space;}x^{(i)}" title="https://latex.codecogs.com/svg.image?{\theta_1}:={\theta_1}-{\alpha}\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})\text{ }\cdot\text{ }x^{(i)}" />


Simultaneously update the parameters until convergence and select the proper value for the learning rate alpha.

If alpha is too big, the algorithm can overshoot the minimum (it may fail to converge or diverge). [left image]

If alpha is too small, the algorithm converges to the minimum at a slow rate. [right image]

![Learning Rate Alpha](/img/learning_rate_alpha.PNG?raw=true "Learning Rate Alpha")


## Linear Regression (Multiple Variables)


## Hypothesis

The linear regression model for multiple variables is:

<img src="https://latex.codecogs.com/svg.image?{\color{white}h_{\theta}(x)=\theta_0&plus;\theta_1x_1&plus;\theta_2x_2&plus;...&plus;\theta_nx_n" title="https://latex.codecogs.com/svg.image?h_{\theta}(x)=\theta_0+\theta_1x_1+\theta_2x_2+...+\theta_nx_n" />

## Parameters

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta\text{&space;for&space;n&plus;1&space;dimensional&space;vector}" title="https://latex.codecogs.com/svg.image?\theta\text{ for n+1 dimensional vector}" />

## Cost Function

<img src="https://latex.codecogs.com/svg.image?{\color{white}J(\theta)=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}x^{(i)}-y^{(i)})^2" title="https://latex.codecogs.com/svg.image?J(\theta)=\frac{1}{2m}\sum_{i=1}^{m}(h_{\theta}x^{(i)}-y^{(i)})^2" />

## Gradient Descent

Repeat simultaneously update every j=0, ..., n

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta_j:=\theta_j\alpha\frac{\delta}{\delta\theta_j}J(\theta)" title="https://latex.codecogs.com/svg.image?\theta_j:=\theta_j\alpha\frac{\delta}{\delta\theta_j}J(\theta)" />

## Normal Equation

The closed-form solution to linear regression. Using the formula below, you don't require any feature scaling to calculate the parameters theta and there's no need for calculation of gradient descent.

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta=(X^TX)^{-1}X^T{\vec{y}}" title="https://latex.codecogs.com/svg.image?\theta=(X^TX)^{-1}X^T{\vec{y}}" />