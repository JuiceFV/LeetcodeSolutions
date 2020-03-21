# The Solution of the [Two Sum](https://leetcode.com/problems/two-sum/) peoblem <!-- omit in toc -->
Here I represent my solution and explanations for the first [leetcode'](https://leetcode.com/) problem. 

My solution is virtually fastest:

![image](https://user-images.githubusercontent.com/35202460/77234735-e438a880-6bc1-11ea-9b90-ac085332f3bc.png)

However inferior in memory:

![image](https://user-images.githubusercontent.com/35202460/77234785-311c7f00-6bc2-11ea-818e-a301b9572225.png)


## Table of Content <!-- omit in toc -->
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [The Explanations](#the-explanations)
		- [Bruteforce](#bruteforce)
		- [Hash-Map](#hash-map)
## The Problem

### The task <!-- omit in toc -->
Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have ***exactly*** one solution, and you may not use the *same* element twice.

### The examples <!-- omit in toc -->

> Given nums = [2, 7, 11, 15], target = 9,
>
> Because nums[**0**] + nums[**1**] = 2 + 7 = 9,
> return [**0**, **1**].

## The Solution

I was using the Python3 for this task.
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {str(nums[0]): 0}
        for i in range(1, len(nums)):
            supposed_index = dict.get(str(target-nums[i]))
            if supposed_index != None:
                return ([supposed_index, i])
            else:
                dict.update({str(nums[i]): i})
```

## The Explanations

### Condition <!-- omit in toc -->
let's consider the condtion:
1. We have two arrays of **integers**
2. We have a *target* which is also **integer**
3. Each input has only one solution and it's important
4. Receive a pair [***i***, ***j***] whereas ***array[i] + array[j] = target***
5. Considering that  ***i*** $\neq$ ***j***

### Ideas' Drafts <!-- omit in toc -->

#### Bruteforce
<details open> 
<summary>Method explanations</summary>
The first idea arossed was the simple brutforce.
It means that each element add up to the rest elements until the 5th point in the [condition](#condition) (*array[i] + array[j] = target*) is not false.

The algorithm is pretty simple:
$$
\begin{cases}
	return[i,j], & array[i] + array[j] = target \\ i = i + 1, & array[i] + array[j] \neq target \\j = j + 1 & i = n
\end{cases},
$$
where
$$
\begin{cases}
	array \in \Zeta^n \\ i, j \in [0; n-1] \\ target \in \Zeta
\end{cases},
$$

![image](https://user-images.githubusercontent.com/35202460/77233103-50adaa80-6bb6-11ea-863f-542757a0ead2.png)

Let's measure time complexity of this method.
If we need to go throughout the entire array and add up each element then in the worst case we'll find out a solution at the end of the array, specifically the solution will ***i = n - 2*** and ***j = n - 1*** in this case the complexity is $O((n-2)(n-1))$ or $O(n^2)$

Ok, let's just take a step beyond the ordinary thinking.
</details>

#### Hash-Map

<details open> 
<summary>Method explanations</summary>
Just remember that hash-map find-complexity is $O(1)$.
According this knowledge we can just use its complexity for our purposes. For instance we could to thrust something into the hash-map and derive it whenever we want. My idea is simple, I will describe it using math:

$$
\begin{cases}
	return[i,j], & \exist hm[key](target - array[i] = key) \\ \begin{cases}
		i = i + 1 \\ key = array[i] \\ hm[key] = i
	\end{cases}, & \nexists hm[key](target - array[i] = key)
\end{cases},
$$
where
$$
\begin{cases}
	array \in \Zeta^n \\ i \in [1; n-1] \\ 
	hm - hash \ map \  where \ \textit{\textbf{key}} \ is \ \textit{\textbf{array[i]}} \ and \ \textit{\textbf{hm[key]}} \ is \ \textit{\textbf{i}}
\end{cases},
$$
In other words, we're look for the element equal to the (*target - array[i]*), if we are within an array  and didn't find such *array[i]* then we're paste the *array[i]* and *i* into the hash map. It will look like that *hm[array[i]] = i*.

![image](https://user-images.githubusercontent.com/35202460/77234365-ca499680-6bbe-11ea-8643-ec994581495a.png)

Let's compute the complexity of this method.
Due to we are going throughout an array only once $O(n)$
and complexity of hash map deriving is $O(1)$ we get the whole complexity in the wors case $O(n+1)$ or $O(n)$
</details>
