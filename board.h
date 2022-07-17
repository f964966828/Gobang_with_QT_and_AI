#include <vector>

class board{
public:
    board();
    bool set(std::pair<int,int> pos);
    bool check(std::pair<int,int> pos);
    void show_grid();

private:
    std::vector<std::vector<int> > grid;
};