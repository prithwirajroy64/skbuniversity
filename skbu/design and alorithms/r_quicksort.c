#include<stdio.h>
#include <stdlib.h>
#include <time.h>
int partition(int arr[],int l,int r){
	int Pivot=arr[r];
	int i=(l- 1);
	int j;
	for(j=l;j<=r-1;j++){
		if(arr[j]<Pivot){
			i++;
			int temp=arr[i];
			arr[i]=arr[j];
			arr[j]=temp;
		}
	}
	int temp=arr[i+1];
	arr[i+1]=arr[r];
	arr[r]=temp;
	return (i+1);	
}

int R_partition(int arr[],int l,int r){
	srand(time(0));
	int i=l+rand()%(r-l);
	int temp=arr[i];
	arr[i]=arr[r];
	arr[r]=temp;
	return partition(arr,l,r);
}

void QuickSort(int arr[],int l,int r){
	if (l<r){
		int PivotI=R_partition(arr,l,r);
		QuickSort(arr,l,PivotI-1);
		QuickSort(arr,PivotI+1,r);
	}
}
void printArray(int arr[],int n){
	int i;
	for(i=0;i<n;i++){
		printf("%d, ",arr[i]);
	}
	printf("\n");
}
int main(){
	int arr[]={34, 20, 80, 40, 50};
	int n=sizeof(arr)/sizeof(arr[0]);
	printf("Original Array:\n");
	printArray(arr,n);
	QuickSort(arr,0,n-1);
	printf("Sorted Array:\n");
	printArray(arr,n);
	getchar();
	return 0;
}
