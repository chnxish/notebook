#ifndef DATA_STRUCTURE_LINK_STACK_
#define DATA_STRUCTURE_LINK_STACK_

#include "node.h"

template <typename ElemType>
class LinkStack {
    public:
        LinkStack();
        LinkStack(const ElemType *elems, int n);
        ~LinkStack();
        LinkStack(const LinkStack &other);
        LinkStack& operator=(const LinkStack &other);
        bool Empty() const;
        void Clear();
        void Push(const ElemType &e);
        bool Pop(ElemType &e);
        bool GetTop(ElemType &e);
        int GetLength() const;
        void Traverse(void (*visit)(const ElemType &e)) const;

    private:
        Node<ElemType> *head_;
        int length_;
};

template <typename ElemType>
LinkStack<ElemType>::LinkStack() {
    head_ = new Node<ElemType>;
    length_ = 0;
}

template <typename ElemType>
LinkStack<ElemType>::LinkStack(const ElemType *elems, int n) {
    head_ = new Node<ElemType>;
    for (int i = 0; i < n; i++) {
        Node<ElemType> *p = new Node<ElemType>(elems[i]);
        p->next = head_->next;
        head_->next = p;
    }
    length_ = n;
}

template <typename ElemType>
LinkStack<ElemType>::~LinkStack() {
    Clear();
    delete head_;
}

template <typename ElemType>
LinkStack<ElemType>::LinkStack(const LinkStack &other) {
    length_ = other.length_;
    head_ = new Node<ElemType>;
    Node<ElemType> *q = other.head_->next, *p = head_;
    while(q) {
        p->next = new Node<ElemType>(q->data);
        q = q->next;
        p = p->next;
    }
}

template <typename ElemType>
LinkStack<ElemType>& LinkStack<ElemType>::operator=(const LinkStack<ElemType> &other) {
    Clear();
    length_ = other.length_;
    Node<ElemType> *q = other.head_->next, *p = head_;
    while(q) {
        p->next = new Node<ElemType>(q->data);
        q = q->next;
        p = p->next;
    }
    return *this;
}

template <typename ElemType>
bool LinkStack<ElemType>::Empty() const {
    if (length_ == 0)
        return true;
    else
        return false;
}

template <typename ElemType>
void LinkStack<ElemType>::Clear() {
    length_ = 0;
    Node<ElemType> *p = head_->next;
    while(p) {
        head_->next = p->next;
        delete p;
        p = head_->next;
    }
}

template <typename ElemType>
void LinkStack<ElemType>::Push(const ElemType &e) {
    Node<ElemType> *p = new Node<ElemType>(e);
    p->next = head_->next;
    head_->next = p;
    length_++;
}

template <typename ElemType>
bool LinkStack<ElemType>::Pop(ElemType &e) {
    Node<ElemType> *p = head_->next;
    head_->next = p->next;
    e = p->data;
    delete p;
    length_--;
}

template <typename ElemType>
bool LinkStack<ElemType>::GetTop(ElemType &e) {
    Node<ElemType> *p = head_->next;
    e = p->data;
}

template <typename ElemType>
int LinkStack<ElemType>::GetLength() const {
    return length_;
}

template <typename ElemType>
void LinkStack<ElemType>::Traverse(void (*visit)(const ElemType &e)) const {
    Node<ElemType> *p = head_->next;
    while(p) {
        (*visit)(p->data);
        p = p->next;
    }
}

#endif
