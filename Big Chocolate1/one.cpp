#include <bits/stdc++.h>
using namespace std;
 
using int64 = long long;
#define MOD 1000000007
 
int32_t main(){
    int64 A,B;
    cin >> A >> B;
    
    int64 answer = 0;
    for(int64 i = 1; i * i<= A; i++) {
        if(A % i != 0) continue;
        int64 value = A/i;
        
        int64 sum;
        
        if((value & (value -1)) == 0){
            sum = 2 * (i + (value * B));
            answer = max(answer,sum);
            }
            
        if((i & (i -1)) == 0){
            sum = 2 * (value + (i * B));
            answer = max(answer,sum);
            }
        }
        
        for(int64 i = 1; i * i<= B; i++) {
        if(B % i != 0) continue;
        int64 value = B/i;
        
        int64 sum;
        
        if((value & (value -1)) == 0){
            sum = 2 * (i + (value * A));
            answer = max(answer,sum);
            }
            
        if((i & (i -1)) == 0){
            sum = 2 * (value + (i * A));
            answer = max(answer,sum);
            }
        }
        
        cout<<answer << endl;
    
    }
