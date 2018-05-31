package main

import (
	"fmt"
	"sort"
)

/*
	sort包中实现了３种基本的排序算法：插入排序．快排和堆排序．和其他语言中一样，这三种方式都是不公开的，
	他们只在sort包内部使用．所以用户在使用sort包进行排序时无需考虑使用那种排序方式，sort.Interface定义的三个方法：
	获取数据集合长度的Len()方法、比较两个元素大小的Less()方法和交换两个元素位置的Swap()方法，
	就可以顺利对数据集合进行排序。sort包会根据实际数据自动选择高效的排序算法。
*/
type SortParams []int

func (a SortParams) Len() int      { return len(a) }
func (a SortParams) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a SortParams) Less(i, j int) bool {
	return a[i] < a[j]
}

func main() {
	param := []int{656, 66, 56, 23, 9, 1}
	sort.Sort(sort.Reverse(SortParams(param)))
	// sort.Reverse(SortParamsPBNP(param))
	// sort.Sort(SortParamsPBNP(param))
	// sort.Reverse(sort.Sort(SortParamsPBNP(param))) // error:  used as value
	/*
		大概是因为sort.Sort()无返回 不能作为sort.Reverse的参数
		所以升序就直接sort.Sort(SortParams(param))
		降序就———sort.Sort(sort.Reverse(SortParams(param)))
	*/
	fmt.Println(param)
}
