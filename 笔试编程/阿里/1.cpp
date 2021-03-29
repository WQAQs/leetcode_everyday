// 第一题
// n副扑克，张数为m，大小为1～m，每幅扑克抽一张，求和恰好为k的组合数，结果对10e9+7取余数。
// 思路：动态规划。和为i，j副扑克，，dp[i][j] = dp[i-1][j-1]+...+dp[i-m][j-1](此处需要判断 i-m>0 )。初始化，j=1，i<=m,dp[i][j] = 1; i==j,dp[i][j] = 1,后面的情况不可能存在，所以推出循环。

public class Main {
static long MOD = 1000000007;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int k = scanner.nextInt();
            System.out.println(solution(m, n, k));
        }
    }

    public static int solution(int m, int n, int k) {
        if (k < n || k > n * m) return 0;
        long[][] dp = new long[k + 1][n + 1];
        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) {
                    dp[i][j] = 1;
                    //后面的结果不可能发生
                    break;
                } else if (j == 1) {
                    if (i <= m) dp[i][j] = 1;
                } else {
                    for (int p = 1; p <= m; p++) {
                        if (i - p <= 0)
                            break;
                        dp[i][j] += dp[i - p][j - 1];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }
        return (int) (dp[k][n] % MOD);
    }
}



第二题




// 第一题 O(n*m*k) 二维dp
// 第二题 O(nlogn) sort+前缀和


// 数据规模：n, m < 100000, 暴力O(n^2)显然超时，所以我们得考虑nlogn或者线性算法才能AC

// 1. 我们选择一组零件(i,j) 应该是 选择min(a[i]+b[j], a[j]+b[i])作为当前组合的不稳定性
// 2. 那么由1可知当 a[i]+b[j] < a[j]+b[i] 时，应该选择左边的组合，移项得a[i]-b[i] < a[j] - b[j]，移项的想法是如何得到度量零件本身的属性
// 3. 对所有零件以key=a[i]-b[i]进行排序得到新的顺序s，那么排序后，对于零件i，它与左边的零件组合，它自身应该选择b[i]，与右边的零件组合，它自身选择a[i]
// 4. 所以有ans[i] = b[i] * (i-1) + a[i] * (n-i) + sum_a[1...i-1] + sum_b[i+1...n]
// 5. 至于零件冲突，在输入的时候ans[x]和ans[y]都减去min(a[x]+b[y], a[y]+b[x])即可
// 6. 排序时间复杂度排序O(nlogn)，前缀和处理时间和计算ans时间为O(n)，零件冲突处理O(m)

#include <cstdio>
#include <algorithm>
#include <cstring>

const int N = 100005;
int n, m;
int a[N], b[N], id1[N], id2[N];
int u[N], v[N];

int p;
long long suma, sumb, ans[N];

bool cmp1(int x, int y)
{
    return a[x] - b[x] < a[y] - b[y];
}
bool cmp2(int x, int y)
{
    return u[x] < u[y];
}
int main()
{
// freopen("data.in", "r", stdin);
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d%d", &a[i], &b[i]);
        id1[i] = i;
    }
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &u[i], &v[i]);
        --u[i];
        --v[i];
        id2[i] = i;
    }
    for (int i = 0; i < m; ++i)
    {
        u[i + m] = v[i];
        v[i + m] = u[i];
        id2[i + m] = i + m;
    }
    m <<= 1;
    std::sort(id1, id1 + n, cmp1);
    std::sort(id2, id2 + m, cmp2);

// for (int i = 0; i < n; ++i)
//  printf("%d\n", id1[i]);
    p = 0;
    suma = 0;
    for (int i = 1; i < n; ++i)
    {
        sumb += b[id1[i]];
    }
// printf("%lld\n", sumb);

    for (int i = 0; i < n; ++i)
    {
        int idx1 = id1[i];
        int l = 0, r = m, mid, pos;
        while (l < r)
        {
            mid = (l + r) >> 1;
            if (u[id2[mid]] >= idx1)
            {
                r = mid;
                pos = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        while (u[id2[pos]] == idx1)
        {
            ans[idx1] -= std::min(a[idx1] + b[v[id2[pos]]], a[v[id2[pos]]] + b[idx1]);
            ++pos;
        }

        //  if (idx1 == 2)
        //   printf("%lld\n", ans[idx1]);

        //  printf("%d %lld %lld\n", idx1, suma, sumb);

        ans[idx1] += suma;
        ans[idx1] += sumb;
        ans[idx1] += b[idx1] * i;
        ans[idx1] += a[idx1] * (n - i - 1);

        suma += a[idx1];
        sumb -= b[id1[i + 1]];
    }
    for (int i = 0; i < n; ++i)
        printf("%lld\n", ans[i]);

    return 0;
}





#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(n);
    vector<int> del(n);
    int sup = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
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
        // 当 a[i]+b[j] < a[j]+b[i] 时，应该选择左边的组合，移项得a[i]-b[i] < a[j] - b[j]，移项的想法是如何得到度量零件本身的属性
        // 对所有零件以key=a[i]-b[i]进行排序得到新的顺序del，那么排序后，对于零件i，它与左边的零件组合，它自身应该选择b[i]，与右边的零件组合，它自身选择a[i]
        
        // sum[n] - sum[idx] 是del数组[idx, len(del))范围内所有元素的和
        // 因为我们初始化的时候零件i与任意一个零件组合的时候，大家都选的是b
        // 现在，来根据上述思路矫正下初始值即可，矫正过程包括3步：
        // （1）对于del数组中在零件i左边的部分，减去那些零件的b[j]之和，加上那些零件的a[j]之和
        // （2）对于del数组中在零件i右边的部分，减去零件i的b[i]之和，加上零件i的a[i]之和
        ans[i] -= sum[n] - sum[idx];  
        ans[i] -= idx * iDel; 
        ans[i] -= b[i] + a[i];
    }

    for (int i = 0; i < m; ++i) {
         int l, r;
         cin >> l >> r;
         --l; --r;
         int curDel = min(a[l] + b[r], a[r] + b[l]);
         ans[l] -= curDel;
         ans[r] -= curDel;
     }

    for (int i = 0; i < n; ++i)
        cout << ans[i] << " ";
    return 0;
}



