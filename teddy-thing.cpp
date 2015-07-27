class Solution {
public:
    unordered_map<int,int> costs;
    unordered_map<int,int>::iterator got;

    int calcDist(vector<int>& nums, unsigned int start)
    {
        got = costs.find (start);
        if(got != costs.end())
        {
            return costs[start];
        }
        
        if(start == nums.size()-1)
        {
            costs[start]=0;
            return 0;
        }
        int min = INT_MAX;
        for(int i=nums[start];i>0;--i)
        {
            if(start+i<nums.size())
            {
                int temp = 1+calcDist(nums,start+i);
                if(temp<min)
                {
                    min=temp;
                }
            }
        }
        costs[start]=min;
        return min;
    }
    int jump(vector<int>& nums) {
        
        return calcDist(nums,0);
        
    }
};
