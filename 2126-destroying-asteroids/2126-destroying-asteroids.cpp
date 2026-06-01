class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        sort(asteroids.begin(),asteroids.end());
        long long curr_mass=mass;
        for (int asteroid:asteroids) {
            if (curr_mass<asteroid){
                return false;
            }
            curr_mass+=asteroid;
        }
        return true;
        
    }
};