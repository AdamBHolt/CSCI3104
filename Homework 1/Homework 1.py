def OptimalStock():
    Dates = ["8/25/2014","8/26/2014","8/27/2014","8/28/2014","8/29/2014",\
    "9/2/2014","9/3/2014","9/4/2014","9/5/2014","9/8/2014","9/9/2014","9/10/2014",\
    "9/11/2014","9/12/2014","9/15/2014","9/16/2014","9/17/2014","9/18/2014",\
    "9/19/2014","9/22/2014","9/23/2014"]
    
    WFM = [38.49,38.495,39.8,39.185,39.14,39.09,39.045,39.125,39.52,38.81,\
    38.35,38.63,38.51,38.095,37.57,38.19,39.375,39.79,39.17,38.8,38.135]

    GOOG = [584.72,581.26,577.27,569.56,571.33,571.85,580,580,583.98,586.6,\
    588.9,581.5,580.36,581,572.94,572.76,580.01,587,591.5,593.82,586.85]
    
    AMZN = [333.21,337,342.09,340,341.76,339.98,342.54,343.69,346.3,344.54,\
    341.61,334.3,329.94,329.56,330.91,321.07,327.76,325.44,327.6,328.49,322.46]
    
    findMaxSubarray(WFM, Dates)
    
def findMaxSubarray(p, d, low = 0, high = -1):
    if(high == low):
        return (low, high, p[low], d[low])
    else:
        mid = (low + high)//2
        (lLow, lHigh, lSum) = findMaxSubarray(p, d, low, mid)
        (rLow, rHigh, rSum) = findMaxSubarray(p, d, mid+1, high)
        (cLow, cHigh, cSum) = findMaxCrossSubarray(p, d, low, mid, high)
        if((lSum >= rSum) and (lSum >= cSum)):
            return (lLow, lHigh, lSum)
        elif((rSum >= lSum) and (rSum >= cSum)):
            return (rLow, rHigh, rSum)
        else:
            return (cLow, cHigh, cLow)
            
def findMaxCrossSubarray(p, d, low, mid, high):
    lSum = -100000
    sum = 0
    i = mid
    mLeft = 0
    
    for i in range (mid, low, -1):
        sum = sum + p[i]
        if sum > lSum:
            lSum = sum
            mLeft = i

    rSum = -100000
    sum = 0
    j = mid + 1
    mRight = 0
    for j in range (mid + 1, high):
        sum = sum + p[j]
        if sum > rSum:
            rSum = sum
            mRight = j
    return (mLeft, mRight, lSum + rSum)
    
if __name__ == '__main__':
    OptimalStock()
