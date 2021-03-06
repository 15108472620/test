//assignment 1
#include <iostream>
// using namespace std;
template<class T2>
class array
{
private:
    size_t length;
    int * list;
public:
    // array(){
    //     return this->list;
    // };
    
    array(size_t n){
        this->length=n;
    }; //n是数组的长度，初始化后不能变
    array(const array& b){

        this->length=b.length;
        for(int i=0;i<this->length;i++){
            this->list[i]=b.list[i];
        }
    };
    array(array&& b){
        this->length=b.length;
        for(int i=0;i<this->length;i++){
            this->list[i]=b.list[i];
        }
    };

    array(const std::initializer_list<value_type>& l);

    T2 &operator[](const std::initializer_list<value_type>& x){
        return this->list[x];
    }

    ~array(){
        if(this->list!=NULL){
            delete[] this->list;
            this->list=NULL;
        }
    };

	//一下两个重载运算符函数，如果b和this数组长度不同，抛出信息为”difference dimension”的异常，但不终止程序

    array& operator=(const array& b){
        if(this->list!=NULL){
            delete[] this->list;
            this->list=NULL;
            this->length=0;
        }
        this->length=b.length;
        for(int i=0;i<this->length;i++){
            this->list[i]=b.list[i];
        }
        return *this;
    }; 
    array& operator=(array&& b){
        if(this->length!=size(b)){
            std::cout << "different dimension" << std::endl;
        }
        return ;
    };

	//当index超界时，抛出信息为"index out of range"的异常，并终止程序
    reference operator[](size_t index){
        if(index>this->length){
            std::cout << "index out of range" << std::endl;
        }
    };

    constexpr size_t size(array list) const{
        return sizeof(list)/sizeof(int)
    }; //获取数组的长度

    constexpr bool empty() const{
        if(this->list==0){
            return false;
        }
        else {
            return true;
        }
    }; //测试数组是否为空

    void clear(){
        if(this->list!=NULL){
            delete[] this->list;
            this->list=NULL;
        }
    }; //清空数组，保持长度不变

    friend std::ostream& operator <<(std::ostream& os, const array& a);
};

//用类似于[1,2,3,4,5]的格式打印出数组所有元素
std::ostream& operator <<(std::ostream& os, const array& a)
{
    array<int>::iterator it1 = a.begin();
    while(it1!=psd.end()) 
    return os << *it1++ << std::endl;

    array<int>::reverse_iterator it2 = a.rbegin();
    while(it2!=psd.rend()) 
    return os << *it2++ << std::endl;
}


//请不要修改main中任何内容！
int main()
{
    using iarray = array<int>;
    auto print_r = [](iarray& a) {
        for (auto v : a) std::cout << v << ' ';
        std::cout << std::endl;
    };
    
    size_t m, n, i1, i2;
    std::ifstream f("array-test.in", std::ios_base::in);
    f >> m;

    while (m--)
    {
        f >> n;

        iarray a(n);
        for (auto& e : a) f >> e;
        f >> i1 >> i2;

        print_r(a);

        a[i1] = 9;
        print_r(a);

        decltype(a) b(n);
        b = a;
        for (auto i = b.rbegin(); i != b.rend(); --i) std::cout << *i << ' ';
        std::cout << std::endl;

        b = std::move(iarray{-1, -2, -3});

        b[i2] = 10;
        print_r(b);
    }

    f.close();
    
    return 0;
}