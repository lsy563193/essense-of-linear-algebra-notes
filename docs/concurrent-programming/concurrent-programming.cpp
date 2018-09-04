//import time, threading
# include <chrono>
// 假定这是你的银行存款:
#include <catch_with_main.hpp>
#include <range/v3/all.hpp>

using namespace ranges;

TEST_CASE("foreach on lazy range") {
    for(const auto& x : view::ints(0, 6)) {
        std::cout << x * x << std::endl;
    }
}
auto balance = 0;


void change_it(int n){
    // # 先存后取，结果应该为0:
    balance = balance + n;
    balance = balance - n;
}

void run_thread(int n){
    // for i in range(10000000):
    for(auto i : range(10000000))
        change_it(n)/
}

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)