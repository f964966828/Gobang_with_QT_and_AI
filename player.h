#include <vector>

class player{
public:
    player();
    std::pair<int,int> step(std::vector<std::vector<int>> grid);

private:
    int playerID;
};