#ifndef DATA_STRUCTURE_LINK_QUEUE_
#define DATA_STRUCTURE_LINK_QUEUE_

#include "node.h"

template <typename ElemType>
class LinkQueue {
    public:
        LinkQueue();
        LinkQueue(const ElemType *elems, int n);
        ~LinkQueue();
        LinkQueue(const LinkQueue &other);
        LinkQueue& operator=(const LinkQueue &other);
        bool Empty() const;
        void Clear();
        void Push(const ElemType &e);
        void Pop(ElemType &e);
        void GetTop(ElemType &e);
        int GetLength() const;
        void Traverse(void (*visit)(const ElemType &e)) const;

    private:
};

#endif
