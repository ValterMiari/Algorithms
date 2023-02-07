#include <iostream> 
#define HEAP_SIZE 65536 // Arbitrary for now, 2^16

/* A simple mark and sweep algorithm */

// Shouldn't be exposed. For now, it is
struct ObjectHeader {
    size_t size = sizeof(this);
    bool marked = false;
};

struct Object : ObjectHeader {
    //int id;
    char name; // should be something like id, but for testing sake its char
    Object* child;
};

// Representing the heap as a simple struct for now
struct Heap {
    Object heap_space[HEAP_SIZE];
};

// For now it assumes that it is given root objects from the start
// Should, for instance, be a workinglist later
class MarkSweep {
    public:
        void mark(Object* obj) {
            if (!markedBit(obj)) {
                markBit(obj);
                Object* ref = obj->child;
                if (ref != nullptr) {
                    mark(ref);
                }
            }
        }

        void sweep(Heap heap) {
            for (Object obj: heap.heap_space) {
                if (!markedBit(&obj)) {
                    //free(&obj); // this is temporary, should be own impl later
                    delete &obj;
                }
            }
        }

    private:
        bool markedBit(Object* obj) {
            return obj->marked;
        }

        void markBit(Object* obj) {
            obj->marked = true;
        }

};

int main() {
    Object* b = new Object();
    b->name = 'B';
    b->child = nullptr;
    Object* c = new Object();
    c->name = 'C';
    c->child = b; // c -> d
    Object* d = new Object();
    d->name = 'D';
    d->child = nullptr;

    Heap* heap = new Heap{*c, *b, *d};
    MarkSweep gc;
    gc.mark(c);
    std::cout << "Expected 1, got: " << b->marked << '\n';
    std::cout << "Expected 1, got: " << c->marked << '\n';
    std::cout << "Expected 0, got: " << d->marked << '\n';

    // sweep doesn't work yet in the context, since b,c,d is not on in the heap mem.
    gc.sweep(*heap); 
    std::cout << b << '\n';
    std::cout << c->marked << '\n';
    std::cout << d << '\n';

    return 0;
}

