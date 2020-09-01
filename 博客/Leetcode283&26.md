# 算法：26 & 283

Leetcode上面题型类似的题目，这里发现[26题](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)和[283](https://leetcode-cn.com/problems/move-zeroes/)题使用相同的思路

##  283. 移动零

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

实例：

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

## 26. 删除排序数组中的重复项

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例：

```
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
```

## 解法思路

我想，来看题解的同学都是了解了题目的，大致表述一下解题的思路。

我们可以定义两个指针，一个指针指向需要修改的地方，一个指向 修改使用的值的地方。

记住上面这句话，问题就解决了。

### 283：

```java
public void moveZeros(int[] nums){
            /**
             * 输入: [0,1,0,3,12]
             * 输出: [1,3,12,0,0]
             */
            if (nums == null){
                return;
            }
            int j = 0;
            for (int i = 0;i<nums.length;i++){
                if (nums[i]!=0){
                    int tmp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = tmp;
                    j++;
                }
            }
        }
```

### 26:

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}

```

