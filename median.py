import argparse
"""
The function tries to divide the 2 lists into 2 halves such that all the elemnts in the first half are smaller than or equal to all the elemnts in the second half.
If the the last element in first half of a1 is not smaller than the first elemt in  the second half of a2 then we need to select fewer elemmts from a1 and more from b1
A similiar logic applies to a2
We use a binary search like technique to find this partitioning point.
Time Complexity: O(log(min(n,m)))  
"""
def median(a1, a2, i, j):
    start = 0
    end = i
    median = 0
    idx1 = -1 
    idx2 = -1
    while start<=end: #find the partioning in a1
        idx1 = int((start+end)/2) #selects (start+end)/2 elements from the first list
        idx2 = int((i+j+1)/2) - idx1 #selects the remaining num of elemnts from the second list such that they form half of the total elemnts in both the list
        if idx1>0 and idx2<j and a1[idx1-1]>a2[idx2]:
            end = idx1-1
        elif idx2>0 and idx1<i and a2[idx2-1] > a1[idx1]:
            start = idx1+1
        else:
            if idx1 == 0: #all elements in a1 > a2
                median = a2[idx2-1]
            elif idx2==0: #all elemnets in a2 > a1
                median = a1[idx1-1]
            else:
                median = max(a1[idx1-1], a2[idx2-1])
            break

    if((i+j)%2==1): #odd num of elemnts return the middle elemnt
        return median
    else: #even num of elemnts return the average of first element in second half + last element if first half
        if idx1==i: #all elements in a1 < a2
            return float(median+a2[idx2])/2.0
        elif idx2==j: #all elements in a2 < a1
            return float(median+a1[idx1])/2.0
        else:
            return float(median+ min(a1[idx1],a2[idx2]) )/2.0
    

def main(arr1, arr2):
    n = len(arr1)
    m = len(arr2) 
    if(n>m):
        print(median(arr2, arr1, m, n))
    else:
        print(median(arr1, arr2, n, m))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lista", nargs="*", type=int, default=[1,3], help="Enter space separated integers (default: [1,3])")
    ap.add_argument("--listb", nargs="*", type=int, default=[2], help="Enter space separated integers (default: [2])")
    args = ap.parse_args()
    main(args.lista, args.listb)
    # main([7,8,9,10,11,12,13,14,15],[1,2,3])
    # main([],[1,2,3])
    # main([],[1])
    # main([2],[1,3])
    # main([2,4,6,8],[1,3,5,7])