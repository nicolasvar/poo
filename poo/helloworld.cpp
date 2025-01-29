#include <iostream>
#include <string>

class helloworld
{
public:
    helloworld() : name(""){}
    
    std::string sayHello()
    {
        return "Hello, World" + name + "!";
    }
    std::string name;
};

int main()
{
    helloworld object1;
    object1.name = "Nicolas";
    std::cout << object1.sayHello() << std::endl;
    return 0;
}