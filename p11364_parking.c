#include <stdio.h>

int main()
{
    int j, arr[4] = {24,13,89,37};
    // for(j = 0;j<4;j++){
    //     printf("%d ",arr[j]);
    // }
    int i,dist[99];
    for (i = 1;i<=99;i++){
        for(j = 0;j<4;j++){
            dist[i]+=abs(arr[j]-i);
        }
    }
    for(int i = 0;i<99;i++){
        printf("%d ",dist[i]);
    }


    return 0;
}
