#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{

    //1. 创建流
    ifstream input;

    //2. 打开文件，将流与文件相关联
    //3, 3步可以直接合并为：ifstream input("number.txt");
    input.open("data.txt");

    // //4. 从文件读入数据
    // int number1, number2, number3;
    // input >> number1 >> number2 >> number3;

    // cout << "number1: " << number1 << endl;
    // cout << "number2: " << number1 << endl;
    // cout << "number3: " << number1 << endl;
    int n, m;
    input >> n >> m;
    vector<int> a(n), b(n);
    vector<int> del(n);
    int sup = 0;
    for (int i = 0; i < n; ++i) {
        input >> a[i] >> b[i];
        sup += b[i];
        del[i] = b[i] - a[i];
    }

    vector<int> ans(n, sup);

    for (int i = 0; i < n; ++i)
        // 每个零件i的ans结果初始化： 到这里相当于是每一个零件i(0 <= i < n)，和任意一个零件j（包括他自己, 即 0 <= j < n）的不稳定组合都是：
        // i零件,j零件都选择b不稳定性，即都选择空间不稳定性 
        ans[i] += n * b[i];   
      
      
    sort(del.begin(), del.end()); // 依据每个零件的 b[i] - a[i]属性排序

    vector<int> sum(n + 1, 0); 

    for (int i = 0; i < n; ++i)
        sum[i + 1] = sum[i] + del[i]; // sum[i] 表示：del数组(即b[i] - a[i]属性排序数组）前i个元素的和，
        // 例如：sum[0]表示del数组前0个元素的和，即没有元素，所以sum[0]为初始值即 sum[0] = 0
        //      sum[3]表示del数组前3个元素的和，即没有元素，所以 sum[3] = del[0] + del[1] + del[2]

    for (int i = 0; i < n; ++i)
    {
        int iDel = b[i] - a[i];
        // 查找i零件在del数组（ b[i] - a[i]属性排序数组）中的位置，
        // 返回的idx是del数组第一个大于 b[i] - a[i] 的元素索引
        int idx =  upper_bound(del.begin(), del.end(), iDel)- del.begin(); 
            // 注意！iDel 在del数组中的索引即为：idx_iDel = idx - 1
            // 所以这里有个技巧： 就是del数组范围：[0, idx_iDel] 内的元素个数就是idx ，即第一个大于iDel元素的索引的值idx
        
        // 根据思路：        
        // 当 b[i] + a[j] < b[j] + a[i] 时，应该选择左边的组合，移项得b[i] - a[i] < b[j] - a[j]，移项的想法是如何得到度量零件本身的属性
        // 对所有零件以 key=b[i] - a[i] 进行排序得到新的顺序del，那么排序后，
        // 对于零件i，它与左边的零件组合，它自身应该选择a[i]，与右边的零件组合，它自身选择b[i]
        
        // sum[n] - sum[idx] 是del数组[idx, len(del))范围内所有元素的和
        // 因为我们初始化的时候零件i与任意一个零件组合的时候，大家都选的是b
        // 现在，来根据上述思路矫正下初始值即可，矫正过程包括3步：
        // （1）对于del数组中在零件i左边的部分，减去零件i的b[i]之和，加上零件i的a[i]之和
        // （2）对于del数组中在零件i右边的部分，减去那些零件的b[j]之和，加上那些零件的a[j]之和
        ans[i] -= sum[n] - sum[idx];  
        ans[i] -= idx * iDel; 
        ans[i] -= b[i] + a[i];
    }

    for (int i = 0; i < m; ++i) {
         int l, r;
         input >> l >> r;
         --l; --r;
         int curDel = min(a[l] +
          b[r], a[r] + b[l]);
         ans[l] -= curDel;
         ans[r] -= curDel;
     }

    for (int i = 0; i < n; ++i) 
        cout << ans[i] << " ";
    
        //5. 关闭流
    input.close();
    return 0;
}