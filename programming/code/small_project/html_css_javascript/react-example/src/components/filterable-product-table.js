import React from 'react';

import { makeStyles } from '@mui/styles';

import groupingArray from '../util/grouping-array';

const useStyles = makeStyles({
  root: {
    width: '300px',
    margin: 'auto',
    paddingTop: '20px',
    paddingLeft: '50px',
  },
  searchBarInput: {
    height: '20px',
  },
  searchBarLabel: {
    fontSize: '0.9rem',
  },
  productTable: {
    marginTop: '10px',
  },
  productTableTitleSpan: {
    width: '100px', 
    fontWeight: 'bold', 
    display: 'inline-block',
  },
  productCategoryRow: {
    fontWeight: 'bold',
    paddingTop: '2px',
    paddingBottom: '2px',
  },
  productRow: {
    paddingTop: '2px',
    paddingBottom: '2px',
  },
  productRowSpan: {
    width: '100px',
    display: 'inline-block',
  },
});

const globalData = [
  {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
  {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
  {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
  {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
  {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
  {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
];

const processingData = (searchObject, onlyShowStocked) => {
  var data = JSON.parse(JSON.stringify(globalData));
  if (searchObject !== '') {
    for (let i = 0; i < data.length; i++) {
      if (data[i].name.indexOf(searchObject) !== 0) {
        data.splice(i, 1);
        i--;
      }
    }
  }
  if (onlyShowStocked === true) {
    data.forEach(function(item, index, arr) {
      if (item.stocked === false) {
        arr.splice(index, 1);
      }
    });
  }

  data = groupingArray(data, 'category');

  return data;
}

const FilterableProductTable = () => {
  const [searchObject, setSearchObject] = React.useState('');
  const [onlyShowStocked, setOnlyShowStocked] = React.useState(false);

  let data = processingData(searchObject, onlyShowStocked);
  let keys = Object.keys(data);
  const classes = useStyles();

  const handleSearchObjectChange = (value) => {
    setSearchObject(value);
    handleDataChange();
  }

  const handleOnlyShowStockedChange = (checked) => {
    setOnlyShowStocked(checked);
    handleDataChange();
  }

  const handleDataChange = () => {
    data = processingData(searchObject, onlyShowStocked);
    keys = Object.keys(data);
  }

  return (
    <div className={classes.root}>
      <div className="searchbar">
        <input 
          type="text" placeholder="Search..." value={searchObject} className={classes.searchBarInput}
          onChange={(event) => handleSearchObjectChange(event.target.value)} 
        />
        <br />
        <label className={classes.searchBarLabel}>
          <input type="checkbox" checked={onlyShowStocked} onChange={(event) => handleOnlyShowStockedChange(event.target.checked)} />
          Only show products in stock
        </label>
      </div>
      <div className={classes.productTable}>
        <div className="product-table-title">
          <span className={classes.productTableTitleSpan}>Name</span>
          <span className={classes.productTableTitleSpan}>Price</span>
        </div>
        {keys.map(function(k, index) {
            return (
              <div key={index} className={classes.productCategoryRow}>
                {k}
                {
                  data[k].map(function(d, index) {
                    return (
                      <div key={index} className={classes.productRow}>
                        <span className={classes.productRowSpan} style={{ color: d.stocked ? 'black' : 'red' }} >{d.name}</span>
                        <span className={classes.productRowSpan}>{d.price}</span>
                      </div>
                    );
                  })
                }
              </div>
            );
          }
        )}
      </div>
    </div>
  );
};

export default FilterableProductTable;
