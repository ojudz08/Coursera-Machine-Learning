# Logistic Regression

Logistic regression is  mostly used for classification tasks (i.e. classifying spam emails, malignant or benign tumors). 

## Logistic Function (Sigmoid Function) 

We want our predicted model to have a value of between 0 and 1. 

<img src="https://latex.codecogs.com/svg.image?{\color{white}0\leq{h}_{\theta}(x)\leq&space;1" title="https://latex.codecogs.com/svg.image?0\leq{h}_{\theta}(x)\leq 1" />

In order to achieve this, we use the sigmoid function.

<img src="https://latex.codecogs.com/svg.image?{\color{white}g(z)=\frac{1}{1&plus;e^{-z}}" title="https://latex.codecogs.com/svg.image?g(z)=\frac{1}{1+e^{-z}}" />


![Sigmoid](/img/sigmoid.png?raw=true "Sigmoid")

## Hypothesis

The hypothesis will be represented as

<img src="https://latex.codecogs.com/svg.image?{\color{white}h=g(z)" title="https://latex.codecogs.com/svg.image?h=g(z)" />

.

<img src="https://latex.codecogs.com/svg.image?{\color{white}h_{\theta}(x)=g({\theta}^Tx)" title="https://latex.codecogs.com/svg.image?h_{\theta}(x)=g({\theta}^Tx)" />

and when sigmoid function is applied, hypothesis is represented as

<img src="https://latex.codecogs.com/svg.image?{\color{white}h_{\theta}(x)=\frac{1}{1&plus;e^{-\theta^T{x}}}" title="https://latex.codecogs.com/svg.image?h_{\theta}(x)=\frac{1}{1+e^{-\theta^T{x}}}" />


### Cost Function

We use the logarithmic loss function to calculate the cost for the classification problem.

<img src="https://latex.codecogs.com/svg.image?{\color{white}\text{Cost}(h_{\theta}(x),y)=\left\{\begin{aligned}-log(h_{\theta}(x))\text{&space;if&space;}y=1&space;\\-log(1-h_{\theta}(x))\text{&space;if&space;}y=0\end{aligned}\right." title="https://latex.codecogs.com/svg.image?\text{Cost}(h_{\theta}(x),y)=\left\{\begin{aligned}-log(h_{\theta}(x))\text{ if }y=1 \\-log(1-h_{\theta}(x))\text{ if }y=0\end{aligned}\right." />

The cost function can be written as below:

<img src="https://latex.codecogs.com/svg.image?{\color{white}J(\theta)=-\frac{1}{m}\left&space;[&space;\sum_{i=1}^{m}y^{(i)}\text{&space;log&space;}{h_{\theta}}(x^{(i)})\text{&space;&plus;&space;}(1-y^{(i)})\text{&space;log&space;}(1-h_{\theta}(x^{(i)}))&space;\right&space;]" title="https://latex.codecogs.com/svg.image?J(\theta)=-\frac{1}{m}\left [ \sum_{i=1}^{m}y^{(i)}\text{ log }{h_{\theta}}(x^{(i)})\text{ + }(1-y^{(i)})\text{ log }(1-h_{\theta}(x^{(i)})) \right ]" />

### Gradient Descent

Similar to linear regression, the aim is to minimize the cost function,

<img src="https://latex.codecogs.com/svg.image?{\color{white}min_{\theta}J({\theta})" title="https://latex.codecogs.com/svg.image?min_{\theta}J({\theta})" />

Repeat until the parameters converge

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta_j:=\theta_j-{\alpha}\frac{\delta}{\delta\theta_j}J({\theta})" title="https://latex.codecogs.com/svg.image?\theta_j:=\theta_j-{\alpha}\frac{\delta}{\delta\theta_j}J({\theta})" />

.

<img src="https://latex.codecogs.com/svg.image?{\color{white}\frac{{\delta}J{(\theta)}}{\delta\theta_j}=\frac{1}{m}\sum_{i=1}^{m}\left&space;(&space;h_\theta(x^{(i)})&space;-&space;y^{(i)}&space;\right&space;)x_j^{(i)}" title="https://latex.codecogs.com/svg.image?\frac{{\delta}J{(\theta)}}{\delta\theta_j}=\frac{1}{m}\sum_{i=1}^{m}\left ( h_\theta(x^{(i)}) - y^{(i)} \right )x_j^{(i)}" />

.

<img src="https://latex.codecogs.com/svg.image?{\color{white}\theta_j:=\theta_j-\frac{\alpha}{m}\sum_{i=1}^{m}\left&space;(&space;h_\theta(x^{(i)})&space;-&space;y^{(i)}&space;\right&space;)x_j^{(i)}" title="https://latex.codecogs.com/svg.image?\theta_j:=\theta_j-\frac{\alpha}{m}\sum_{i=1}^{m}\left ( h_\theta(x^{(i)}) - y^{(i)} \right )x_j^{(i)}" />