#ifndef CPP_PRIMER_SALES_ITEM_H_
#define CPP_PRIMER_SALES_ITEM_H_

#include <iostream>
#include <string>

class SalesItem {
  friend std::istream& operator>>(std::istream&, SalesItem&);
  friend std::ostream& operator<<(std::ostream&, const SalesItem&);
  friend bool operator<(const SalesItem&, const SalesItem&);
  friend bool operator==(const SalesItem&, const SalesItem&);

 public:
  SalesItem(): units_sold_(0), revenue_(0.0) {};
  SalesItem(const SalesItem& si)
      : book_no_(si.book_no_),
        units_sold_(si.units_sold_),
        revenue_(si.revenue_) {}
  SalesItem(const std::string& book)
      : book_no_(book), units_sold_(0), revenue_(0.0) {}
  SalesItem(std::istream& is)
      : units_sold_(0), revenue_(0.0) { is >> *this; }
  SalesItem& operator+=(const SalesItem&);
  std::string Isbn() const { return book_no_; }
  unsigned GetUnitsSold() const { return units_sold_; }
  double GetRevenue() const {return revenue_; }
  double AvgPrice() const;
 
 private:
  std::string book_no_;
  unsigned int units_sold_;
  double revenue_;
};

SalesItem operator+(const SalesItem&, const SalesItem&);

bool operator!=(const SalesItem& lhs, const SalesItem& rhs);

bool CompareIsbn(const SalesItem& lhs, const SalesItem& rhs);

#endif
