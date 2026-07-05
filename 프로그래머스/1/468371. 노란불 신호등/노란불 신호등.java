class Solution {
    
    int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    
    int lcm(int a, int b) {
        return a / gcd(a, b) * b;
    }
    
    public int solution(int[][] signals) {
        
        int limit = 1;
        
        for(int[] s : signals) {
            int cycle = s[0] + s[1] + s[2];
            limit = lcm(limit, cycle);
        }
        
        for(int t = 1; t < limit; t++) {
            boolean find = true;
            
            for(int[] s: signals) {
                int g = s[0];
                int y = s[1];
                int r = s[2];
                
                int cycle = g + y + r;
                int x = (t-1) % cycle;
                
                if(!(g <= x && x < g + y)) {
                    find = false;
                    break;
                }
            }
            
            if(find) return t;
        }
        
        return -1;
    }
}