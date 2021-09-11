#ifndef DATA_STRUCTURE_LINK_LIST_
#define DATA_STRUCTURE_LINK_LIST_

#include "node.h"

template <typename ElemType>
class LinkList {
    public:
        LinkList();
	    LinkList(const ElemType *elems, int n);
	    ~LinkList();
	    LinkList(const LinkList &other);
	    LinkList& operator=(const LinkList &other);
	    void Clear();
	    int InsertElem(const ElemType &e);
	    int InsertElem(int i, const ElemType &e);
	    int DeleteElem(int i, ElemType &e);
	    int SetElem(int i, const ElemType &e);
        int GetElem(int i, ElemType &e) const;
        int LocateElem(const ElemType &e) const; 
        int GetLength() const;
        void Traverse(void (*visit)(const ElemType &e)) const;

    private:
        Node<ElemType> *head_;
        int length_;
};

template <typename ElemType>
LinkList<ElemType>::LinkList() {
    head_ = new Node<ElemType>;
    length_ = 0;
}

template <typename ElemType>
LinkList<ElemType>::LinkList(const ElemType *elems, int n) {
    head_ = new Node<ElemType>;
    Node<ElemType> *p = head_;
    for (int i = 0; i < n; i++) {
        p->next = new Node<ElemType>(elems[i]);
        p = p->next;
    }
    length_ = n;
}

template <typename ElemType>
LinkList<ElemType>::~LinkList() {
    Clear();
    delete head_;
}

template <typename ElemType>
LinkList<ElemType>::LinkList(const LinkList &other) {
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
LinkList<ElemType>& LinkList<ElemType>::operator=(const LinkList<ElemType> &other) {
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
void LinkList<ElemType>::Clear() {
    length_ = 0;
    Node<ElemType> *p = head_->next;
    while(p) {
        head_->next = p->next;
        delete p;
        p = head_->next;
    }
}

template <typename ElemType>
int LinkList<ElemType>::InsertElem(const ElemType &e) {
    Node<ElemType> *p = head_;
    while(p->next) {
        p = p->next;
    }
    p->next = new Node<ElemType>(e);
    length_++;
    return 1;
}

template <typename ElemType>
int LinkList<ElemType>::InsertElem(int i, const ElemType &e) {
    if (i < 1 || i > length_ + 1)
        return 0;

    Node<ElemType> *p = head_, *q;
    for (int j = 1; j < i; j++)
        p = p->next;
    q = new Node<ElemType>(e, p->next);
    p->next = q;
    length_++;
    return 1;
}

template <typename ElemType>
int LinkList<ElemType>::DeleteElem(int i, ElemType &e) {
    if (i < 1 || i > length_)
        return 0;

    Node<ElemType> *p = head_, *q;
    for (int j = 1; j < i; j++)
        p = p->next;
    q = p->next;
    e = q->data;
    p->next = q->next;
    delete q;
    length_--;
    return 1;
}

template <typename ElemType>
int LinkList<ElemType>::SetElem(int i, const ElemType &e) {
    if (i < 1 || i > length_)
        return 0;

    Node<ElemType> *p = head_->next;
    for (int j = 1; j < i; j++)
        p = p->next;
    p->data = e;
    return 1;
}

template <typename ElemType>
int LinkList<ElemType>::GetElem(int i, ElemType &e) const {
    if (i < 1 || i > length_) 
        return 0;

    Node<ElemType> *p = head_->next;
    for (int j = 1; j < i; j++) 
        p = p->next;
    e = p->data;
    return 1;
}

template <typename ElemType>
int LinkList<ElemType>::LocateElem(const ElemType &e) const {
    Node<ElemType> *p = head_->next;
    int i = 1;
    while (p) {
        if (p->data==e)
            return i;
        else {
            p = p->next;
            i++;
        }
    }
    return 0;
}

template <typename ElemType>
int LinkList<ElemType>::GetLength() const {
    return length_;
}

template <typename ElemType>
void LinkList<ElemType>::Traverse(void (*visit)(const ElemType &e)) const {
    Node<ElemType> *p = head_->next;
    while(p) {
        (*visit)(p->data);
        p = p->next;
    }
}

#endif
