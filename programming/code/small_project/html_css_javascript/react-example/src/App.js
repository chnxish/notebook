import React from 'react';
import './App.css';

import groupingArray from './util/grouping-array';

class ProductCategoryRow extends React.Component {
  render() {
    return (
      <div className="product-category-row">
        {this.props.category}
        {this.props.children}
      </div>
    );
  }
}

class ProductRow extends React.Component {
  render() {
    const color = this.props.stocked ? 'black' : 'red';
    return (
      <div className="product-row">
        <span style={{color: color}} >{this.props.name}</span>
        <span>{this.props.price}</span>
      </div>
    );
  }
}

class ProductTable extends React.Component {
  render() {
    const data = this.props.data;
    let keys = [];
    for (let key in data) {
      keys.push(key);
    }
    return (
      <div className="product-table">
        <div className="product-table-title">
          <span>Name</span>
          <span>Price</span>
        </div>
        {/* <ProductCategoryRow category="123" />
        <ProductRow name="123" price="234" />
        <ProductRow name="123" price="234" /> */}
        {keys.map(function(k, index) {
            return (
              <ProductCategoryRow key={index} category={k}>
              {
                data[k].map(function(d, index) {
                  return (
                    <ProductRow key={index} name={d.name} price={d.price} stocked={d.stocked} />
                  );
                })
              }
              </ProductCategoryRow>
            );
          }
        )}
      </div>
    );
  }
}

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
  }

  handleChange1(event) {
    this.props.hsoc(event.target.value);
  }

  handleChange2(event) {
    this.props.hossc(event.target.checked);
  }

  render() {
    return (
      <div className="searchbar">
        <input type="text" placeholder="Search..." value={this.props.so} onChange={this.handleChange1} />
        <br />
        <label className="searchbar-label">
          <input type="checkbox" checked={this.props.oss} onChange={this.handleChange2} />
          Only show products in stock
        </label>
      </div>
    );
  }
}

class FilterableProductTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchObject: '',
      onlyShowStocked: false
    };
    this.handleSearchObjectChange = this.handleSearchObjectChange.bind(this);
    this.handleOnlyShowStockedChange = this.handleOnlyShowStockedChange.bind(this);
  }

  handleSearchObjectChange(value) {
    this.setState({
      searchObject: value
    });
  }

  handleOnlyShowStockedChange(checked) {
    this.setState({
      onlyShowStocked: checked
    });
  }

  render() {
    let data = JSON.parse(JSON.stringify(this.props.data));
    if (this.state.searchObject !== '') {
      for (let i = 0; i < data.length; i++) {
        if (data[i].name.indexOf(this.state.searchObject) !== 0) {
          data.splice(i, 1);
          i--;
        }
      }
    }
    if (this.state.onlyShowStocked === true) {
      data.forEach(function(item, index, arr) {
        if (item.stocked === false) {
          arr.splice(index, 1);
        }
      });
    }

    data = groupingArray(data, 'category');
    return (
      <div className="filterable-product-table">
        <SearchBar so={this.searchObject} oss={this.onlyShowStocked}
                   hsoc={this.handleSearchObjectChange} hossc={this.handleOnlyShowStockedChange} />
        <ProductTable data={data} />
      </div>
    );
  }
}

function App() {
  const data = [
    {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
    {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
    {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
    {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
    {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
    {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
  ];

  return (
    <FilterableProductTable data={data} />
  );
}

export default App;
